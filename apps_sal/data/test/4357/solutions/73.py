lis = []
li = input().split()
li.sort()
lis.append(li[2] + li[1])
lis.append(li[0])
print(int(lis[0]) + int(lis[1]))
