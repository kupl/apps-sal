n = int(input())
c = list(map(int, input().split()))
t = list(map(int, input().split()))
def d(x): return sorted(x[i + 1] - x[i] for i in range(n - 1))


print('Yes' if c[0] == t[0] and d(c) == d(t) else 'No')
