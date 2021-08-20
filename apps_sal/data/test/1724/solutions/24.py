n = int(input())
a = list(map(int, input().split()))
s = input()
(ans, S) = (0, 0)
for i in range(n):
    if s[i] == '1':
        ans = max(ans + a[i], S)
    S += a[i]
print(ans)
