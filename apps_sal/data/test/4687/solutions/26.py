n, k = list(map(int, input().split()))
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = list(map(int ,input().split()))


judge = 0
dic = {}


for i in range(n):
    if a[i] in dic:
        dic[a[i]] += b[i]
    else:
        dic[a[i]] = b[i]
#print(dic)
dic = list(dic.items())
dic.sort()
#print(dic)


for i in range(10**9):
    if judge >= k:
        print((dic[i-1][0]))
        break
    else:
        judge += int(dic[i][1])
    #print(judge)

