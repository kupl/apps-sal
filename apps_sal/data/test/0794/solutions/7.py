N = int(input())
A = [int(a) for a in input().split()]
if min(A) == max(A):
    print(-1)
else:
    print(*sorted(A))

