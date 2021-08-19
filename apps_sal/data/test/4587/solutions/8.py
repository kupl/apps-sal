import bisect
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
C.sort()
ans = 0
for b in B:
    l = bisect.bisect_left(A, b)
    r = bisect.bisect_right(C, b)
    ans += l * (len(C) - r)
print(ans)
