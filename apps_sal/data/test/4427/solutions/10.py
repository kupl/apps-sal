(r, d, x) = list(map(int, input().split()))
ans = []
for i in range(10):
    x = r * x - d
    ans.append(x)
for i in ans:
    print(i)
