import collections

n = int(input())

li = []


for i in range(n):
    li.append(input())

cnt = collections.Counter(li)
S = cnt.most_common()


C = len(cnt)

li_1 = [S[0][0]]

for i in range(C - 1):
    if S[i][1] == S[i + 1][1]:
        li_1.append(S[i + 1][0])
    else:
        break

li_1.sort()

for i in li_1:
    print(i)
