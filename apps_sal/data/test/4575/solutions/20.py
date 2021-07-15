# ABC092
# 参加者
N = int(input())
# D日間の合宿でX個のチョコが残った
D, X = list(map(int, input().split()))
# 参加者iは,1,Ai+1,2Ai+1..目にチョコを一つ食べる
A = [int(input()) for _ in range(N)]

eaten = 0
for i in range(N):
    day = 0
    cnt = 0
    while True:
        day = A[i]*cnt + 1
        if day <= D:
            eaten += 1
            cnt += 1
        else:
            break
print((eaten+X))

