from bisect import bisect_left, bisect_right

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()

ans = 0
for i in range(n):
    b = B[i]
    pos_a = bisect_left(A, b)
    pos_c = bisect_right(C, b)
    ans += pos_a * (n - pos_c)
print(ans)
