N,K=map(int,input().split())
A = list(map(int,input().split()))
val_memo = {}
for i in range(N):
    if A[i] in val_memo:
        val_memo[A[i]] += 1
    else:
        val_memo[A[i]] = 1

val_memo = sorted(val_memo.items(), key=lambda x: x[0])
total = N-val_memo[0][1]
if total%(K-1):
    print(total//(K-1)+1)
else:
    print(total//(K-1))
