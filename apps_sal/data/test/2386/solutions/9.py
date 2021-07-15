N = int(input())
A = list(map(int,input().split()))
A.insert(0,0)
B = [A[i]-i for i in range(N+1)]
B.pop(0)
B = sorted(B)
if N%2==1:
    b = B[N//2]
    cnt = 0
    for i in range(N):
        cnt += abs(B[i]-b)
else:
    b1 = B[N//2-1]
    cnt1 = 0
    for i in range(N):
        cnt1 += abs(B[i]-b1)
    b2 = B[N//2]
    cnt2 = 0
    for i in range(N):
        cnt2 += abs(B[i]-b2)
    cnt = min(cnt1,cnt2)
print(cnt)
