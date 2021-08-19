N = int(input())
A = list(map(int, input().split()))

# 辞書型を使い、valueでソートする
dic = {}
for i in range(N):
    dic[i] = A[i]

dic = sorted(dic.items(), key=lambda x: x[1])
for d in dic:
    print(d[0] + 1, end=" ")
