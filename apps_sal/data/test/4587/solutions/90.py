import bisect
n = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
C = sorted(list(map(int, input().split())))

cnt = 0
for b in B:
    i = bisect.bisect_left(A, b)
    j = n-bisect.bisect_right(C, b)
    cnt += i*j

print(cnt)

