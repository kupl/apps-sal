n, k = map(int, input().split())
compulsory = list(map(int, input().split()))

answer = [[] for _ in range(1000)]
mark = [False for _ in range(1000)]


for i in range(len(compulsory)):
    mark[compulsory[i]] = True
    answer[i].append(compulsory[i])

k1 = 0
j = 0
for i in range(1, n * k + 1):
    if mark[i]:
        continue
    answer[k1].append(i)
    j += 1
    if j % (n - 1) == 0:
        k1 += 1

for i in range(k):
    for temp in answer[i]:
        print(temp, end=" ")
    print()
