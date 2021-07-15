n = int(input())
a = list(map(int, input().split()))
ans = [0 for _ in range(n)]
for i in a:
    ans[i-1] += 1

for m in ans:
    print(m)

