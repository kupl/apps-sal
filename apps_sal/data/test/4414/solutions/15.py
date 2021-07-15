q = int(input())
ans = ['NO'] * q
for i in range(q):
    a, b, n, s = map(int, input().split())
    if a * n + b >= s and b >= s % n:
        ans[i] = "YES"
for x in ans:
    print(x)
