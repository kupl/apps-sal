import bisect
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()
pat = 0
for i in B:
    numA = bisect.bisect_left(A, i)
    numC = bisect.bisect(C, i)
    pat += numA * (len(C) - numC)
print(pat)
