input(); x = 1; *A, = map(int, input().split())
if 0 in A: print(0); return
for a in A:
    x *= a
    if x > 10**18: print(-1); return
print(x)
