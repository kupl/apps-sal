s = input()
k = int(input())
n = len(s)
if k >= n:
    print(int(2 * ((n + k) // 2)))
    raise SystemExit
ll = 0
for i in range(k + 1):
    for l in range((n + i) // 2, i - 1, -1):
        if s[n - (l - i):n] == s[n + i - 2 * l:n - l]:
            if l > ll:
                ll = l
            break
j = ll
while 2 * j <= n:
    j = j + 1
    for i in range(n - 2 * j):
        if s[i:i + j] == s[i + j:i + 2 * j]:
            ll = j
            break
print(int(2 * ll))
