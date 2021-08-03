A, B, K = map(int, input().split())
a = range(A, B + 1)
for i in sorted(set(a[:K]) | set(a[-K:])):
    print(i)
