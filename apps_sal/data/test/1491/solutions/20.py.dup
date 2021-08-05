n = int(input())
def f(x): return min(x - int(x**0.5)**2, (int(x**0.5) + 1)**2 - x)


a = sorted([[f(int(i)), int(i)] for i in input().split()])
ans = sum(i[0] for i in a[:n // 2]) + sum((int(i[1]**0.5)**2 == i[1]) + (i[1] == 0) for i in a[n // 2:])
print(ans)
