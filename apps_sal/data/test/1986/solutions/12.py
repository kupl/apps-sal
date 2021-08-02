n, k = list(map(int, input().split()))
f = [list(map(int, input().split())) for i in range(n)]

print(sorted(v[0] if v[1] <= k else v[0] - (v[1] - k) for v in f)[-1])
