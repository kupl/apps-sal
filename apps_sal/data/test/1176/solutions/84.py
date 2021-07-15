N = int(input())
A = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if A[i] < 0:
        cnt += 1
A = [abs(a) for a in A]
if cnt % 2 == 0:
    print(sum(A))
else:
    print(sum(A)-2*min(A))
