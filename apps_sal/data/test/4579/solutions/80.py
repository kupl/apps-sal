N = int(input())
S = [input() for _ in range(N)]

dic = {}
for i in range(N):
    dic[S[i]] = 0

print((len(list(dic.keys()))))
