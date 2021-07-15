n = int(input())
A = sorted(list(map(int, input().split())))[::-1]

if n % 2 == 0:
    print(sum(A[:n//2] * 2) - A[0])
else:
    print(sum(A[:n//2] * 2) - A[0] + A[n//2])
