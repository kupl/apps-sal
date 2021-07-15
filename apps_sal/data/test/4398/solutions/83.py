N = int(input())
S, T = map(str, input().split())

# Sの各文字とTの各文字を先頭から順に交互に文字を並べ、新しい文字列を作ります。

answer =  ''
for i in range(N):
    answer += S[i] + T[i]

print(answer)
