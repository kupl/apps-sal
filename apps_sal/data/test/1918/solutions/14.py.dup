n = int(input())
power = list(map(int, input().split()))
s = input()
cnt = 0
for i in range(n):
    if s[i] == 'B':
        cnt += power[i]
ans = cnt
k = cnt
for i in range(n):
    if s[i] == 'B':
        k -= power[i]
    else:
        k += power[i]
    ans = max(ans, k)

k = cnt
for i in range(n - 1, -1, -1):
    if s[i] == 'B':
        k -= power[i]
    else:
        k += power[i]
    ans = max(ans, k)
print(ans)
