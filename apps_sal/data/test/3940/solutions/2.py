(n, m) = map(int, input().split())
mex = 10000000
for i in range(m):
    (a, b) = map(int, input().split())
    mex = min(mex, b - a)
mex = mex + 1
print(mex)
num = 0
x = ' '.join([str(i % mex) for i in range(n)])
print(x)
