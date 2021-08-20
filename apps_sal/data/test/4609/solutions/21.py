N = int(input())
A = [int(input()) for _ in range(N)]
dic = {}
for i in range(N):
    if A[i] in dic.keys():
        dic[A[i]] += 1
    else:
        dic[A[i]] = 1
cnt = 0
for j in dic.keys():
    if dic[j] % 2 == 1:
        cnt += 1
print(cnt)
