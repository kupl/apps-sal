N = int(input())
z = []
w = []
for _ in range(N):
    (x, y) = map(int, input().split())
    z.append(x + y)
    w.append(x - y)
z.sort()
w.sort()
ans = max(abs(z[-1] - z[0]), abs(w[-1] - w[0]))
print(ans)
