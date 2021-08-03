S = input()

# Sの部分文字列は、空文字列以外に N+(N−1)+(N−2)+...+1 = N(N+1)/2 個存在する
# 今回は N<=10 であり、この個数は最大で 10(10+1)/2 = 55 なので間に合う
# 全て調べて、最も長い「ACGT文字列」の長さを求める
# ここで「ACGT 文字列」は、A,C,G,Tのいずれかから成る文字列

N = len(S)
ans = 0
for i in range(N):
    for j in range(i, N):
        T = list(S[i:j + 1])
        M = j - i + 1
        # ACGT文字列かどうかの判定
        flag = True
        for k in range(M):
            if T[k] != 'A' and T[k] != 'C' and T[k] != 'G' and T[k] != 'T':
                flag = False
                break
        # ACGT文字列なら長さを更新
        if flag:
            ans = max(ans, M)

print(ans)
