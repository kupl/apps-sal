a, b, k = map(int, input().split())
c = min(a, b)
cnt = 0
ans = []
for i in range(1, c + 1):
    if a % i == 0 and b % i == 0:
        ans.append(i)
print(ans[-k])
