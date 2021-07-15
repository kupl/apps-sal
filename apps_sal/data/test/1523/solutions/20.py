N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
rec = [[] for i in range(K)]
for i in range(N):
    rec[a[i] - 1].append(i)

S = 0
rec2 = []
num = 0
for i in range(K):
    if len(rec[i]) > 0:
        S += 1
    if len(rec[i]) >= 1:
        rec[i] = sorted(rec[i], key=lambda x: -b[x])
        rec2 += rec[i][1:]

rec2 = sorted(rec2, key=lambda x: b[x])
for i in range(K - S):
    num += b[rec2[i]]

print(num)
