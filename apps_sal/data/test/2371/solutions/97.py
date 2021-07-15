N,Z,W = map(int,input().split())
a_ls = list(map(int, input().split()))

iA = [0] * N
iB = [0] * N

iA[N-1] = abs(a_ls[N-2]-a_ls[N-1])
iB[N-1] = abs(a_ls[N-2]-a_ls[N-1])

# 「次がi番目のカード」という状況でAorBに回ってくる
for i in range(N-2,-1,-1):
    # i番目がAの場合
    if i != 0:
        prev = a_ls[i-1]
    else:
        prev = W
    
    ans = -float('inf')
    # j := 次がj番目、という状態で相手に渡す
    for j in range(i+1,N):
        #print("渡す",j)
        ans = max(ans,iB[j])
    # Aがゲームを終了させる場合
    ans = max(ans,abs(prev-a_ls[-1]))
    iA[i] = ans
    
    # i番目がBの場合
    if i != 0:
        prev = a_ls[i-1]
    else:
        prev = Z

    ans = float('inf')
    # j := 次がj番目、という状態で相手に渡す
    for j in range(i+1,N):
        ans = min(ans,iA[j])
    # Bがゲームを終了させる場合
    ans = min(ans,abs(prev-a_ls[-1]))
    iB[i] = ans

if N != 1:
    print(iA[0])
else:
    print(abs(W-a_ls[0]))
