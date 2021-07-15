n = int(input())
s = input().strip()
a = [0] * (n + 1)
m = [0] * (n + 1)
for i in range(n):
    a[i] = a[i-1] + (1 if s[i] == "(" else -1)
    m[i] = min(m[i-1], a[i])
ans = 0
mm = a[n - 1]
for j in range(n - 1, -1, -1):
    mm = min(mm, a[j])
    if s[j] == "(":
        ans += a[n - 1] == 2 and mm == 2   and m[j - 1] >= 0
    else:
        ans += a[n - 1] == -2 and mm == -2 and m[j - 1] >= 0



print(ans)
