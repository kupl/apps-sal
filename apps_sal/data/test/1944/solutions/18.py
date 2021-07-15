n = int(input())
t = sorted(tuple(map(int, input().split())) for i in range(n))
print('Happy Alex' if any(t[i + 1][1] < t[i][1] for i in range(n - 1)) else 'Poor Alex')
