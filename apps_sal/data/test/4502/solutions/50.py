N = int(input())
A = list(map(int, input().split()))


ans = None
if N % 2 == 1:
    ans = A[::2][::-1] + A[1::2]
else:
    ans = A[1::2][::-1] + A[::2]
print(*ans)
