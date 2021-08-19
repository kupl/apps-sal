import bisect
_ = input()
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]
A.sort()
C.sort()
ans = 0
for b in B:
    a = bisect.bisect_left(A, b)
    c = len(C) - bisect.bisect_right(C, b)
    ans += a * c
else:
    print(ans)
