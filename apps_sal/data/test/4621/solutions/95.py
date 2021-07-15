import copy
h,w = map(int,input().split())
li = []
for i in range(h):
    li.append(input())
#print(li)
lis = copy.copy(li)
#print(lis)
#list1 = li+lis
#print(list1)
for i in range(h):
    print(li[i])
    print(lis[i])
