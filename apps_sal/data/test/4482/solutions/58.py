N = input()
list1 = list(map(int,input().split()))
list2 = []
for i in range(min(list1),max(list1)+1):
    a = 0
    for j in range(len(list1)):
        a += (list1[j] - i)**2
    list2.append(a)
print(min(list2))
