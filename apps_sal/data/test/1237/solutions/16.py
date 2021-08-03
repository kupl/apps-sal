n, s = list(map(int, input().split()))
cf, ct = s, 0
for f, t in sorted((list(map(int, input().split())) for i in range(n)), reverse=True):
    ct = max(ct + cf - f, t)
    cf = f
print(ct + cf)
