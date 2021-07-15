N = int(input())
A = sorted(list(map(int, input().split())))

if A[0] == A[-1]:
    print(-1)
else:
    print(" ".join(map(str, A)))
