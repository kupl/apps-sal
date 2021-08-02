n, k = map(int, input().split())
ans = [0] * (10**5 + 1)
for i in range(n):
    a, b = map(int, input().split())
    ans[a] += b

for i in range(len(ans)):
    k -= ans[i]
    if k <= 0:
        print(i)
        break
