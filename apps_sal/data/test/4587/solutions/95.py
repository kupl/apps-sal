import bisect
n = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))
C = list(map(int, input().split(' ')))

A.sort()
B.sort()
C.sort()
ans = 0
for j in range(n):
    i = bisect.bisect_left(A, B[j])
    k = n - bisect.bisect_right(C, B[j])
    ans += int(i * k)
print(ans)
