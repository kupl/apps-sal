N = int(input())
*A, = map(int, input().split())

if N % 2 == 0:
    print(' '.join(map(str, A[1::2][::-1] + A[::2])))
else:
    print(' '.join(map(str, A[::2][::-1] + A[1::2])))
