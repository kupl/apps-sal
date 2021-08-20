import copy
(h, w) = map(int, input().split())
li = []
for i in range(h):
    li.append(input())
lis = copy.copy(li)
for i in range(h):
    print(li[i])
    print(lis[i])
