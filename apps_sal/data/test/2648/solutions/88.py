N = int(input())
A = list(map(int, input().split()))

kind = len(set(A))
if (N - kind) % 2 == 0:
    print(kind)
else:
    print(kind - 1)
