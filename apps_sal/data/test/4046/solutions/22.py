n = int(input())
q = list(map(int, input().split()))
ans = [0 for i in range(n)]
ans[0] = 1
for i in range(1, n):
    ans[i] = ans[i - 1] + q[i - 1]
t = 1 - min(ans)
b = [i for i in range(1, n + 1)]
x = set(b)
ann = []
for i in ans:
    ann.append(i + t)
    x.discard(i + t)
if len(x):
    print(-1)
else:
    print(*ann)
