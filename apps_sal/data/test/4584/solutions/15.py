n = int(input())
a = list(map(int, input().split()))
ans = [0] * (n + 1)

for i in range(n - 1):
    ans[a[i]] += 1
ans.pop(0)
for j in ans:
    print(j)
