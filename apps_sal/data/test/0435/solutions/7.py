n, t = map(int, input().split())
s = input()
l = 0
k = 0
ma = 0
for r in range(n):
    if s[r] == 'a':
        if r - l + 1 > ma:
            ma = r - l + 1
    else:
        while k >= t:
            if s[l] == 'b':
                k -= 1
            l += 1
        if r - l + 1 > ma:
            ma = r - l + 1
        k += 1
        k %= r - l + 2
l = 0
k = 0
for r in range(n):
    if s[r] == 'b':
        if r - l + 1 > ma:
            ma = r - l + 1
    else:
        while k >= t:
            if s[l] == 'a':
                k -= 1
            l += 1
        if r - l + 1 > ma:
            ma = r - l + 1
        k += 1
        k %= r - l + 2
print(ma)
