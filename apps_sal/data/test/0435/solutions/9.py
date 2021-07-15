n, k = list(map(int,input().split()))
s = input()
l = 0
r = 0
ans = 0
num = 0
i = 0
while i < n:
    r += 1
    if s[i] == "b":
        num += 1
        if num > k:
            ans = max(ans,i-l)
            while l < n and s[l] != "b":
                l += 1
            l += 1
            num -= 1
    i += 1
ans = max(ans,i-l)

l = 0
r = 0
num = 0
i = 0
while i < n:
    r += 1
    if s[i] == "a":
        num += 1
        if num > k:
            ans = max(ans,i-l)
            while l < n and s[l] != "a":
                l += 1
            l += 1
            num -= 1
    i += 1
ans = max(ans,i-l)

print(ans)

