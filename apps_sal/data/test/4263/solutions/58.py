S = input()

N = len(S)
ans = 0
# Sの部分文字列は、空文字列以外に N+(N−1)+(N−2)+...+1 = N(N+1)/2 個存在する
# 今回は N<=10 であり、この個数は最大で 10(10+1)/2 = 55 なので間に合う
# 全て調べて、最も長い「ACGT文字列」の長さを求める
for i in range(N):
    for j in range(i, N):
        if all('ACGT'.count(c) == 1 for c in S[i:j + 1]):
            ans = max(ans, j - i + 1)

print(ans)
