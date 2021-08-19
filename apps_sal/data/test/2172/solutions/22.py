(n, m) = input().split()
(n, m) = (int(n), int(m))
lis = []
for i in range(m):
    lis.append(input().split())


def decide(lis):
    if len(lis[0]) <= len(lis[1]):
        return lis[0]
    else:
        return lis[1]


dic = {}
for i in range(m):
    dic[lis[i][0]] = decide(lis[i])
lec = input().split()
for i in range(n):
    print(dic[lec[i]], end=' ')
