(A, B, K) = map(int, input().split())
x = range(A, B + 1)
for s in sorted(set(x[:K]) | set(x[-K:])):
    print(s)
