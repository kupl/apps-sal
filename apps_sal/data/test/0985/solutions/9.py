def read(): return list(map(int, input().split()))


n = int(input())
N = 1001
b = [0] * 3000
c = [0] * 3000
for i in range(n):
    x, y = read()
    b[x - y + N] += 1
    c[y + x] += 1


def f(x): return x * (x - 1) // 2


ans = sum(f(i) for i in b) + sum(f(i) for i in c)
print(ans)
