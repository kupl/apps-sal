import bisect

N=int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))

count=0
for i in range(N):
    a_cand = bisect.bisect_right(A,B[i]-1)
    c_cand = N-bisect.bisect_right(C,B[i])
    count += a_cand*c_cand
print(count)

