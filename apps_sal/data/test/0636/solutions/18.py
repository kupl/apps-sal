n, m = map(int,input().split())
list1 = list(map(int, input().split()))
list2 = []
sum = 0
count = len(list1)
for i in range(len(list1)):
    if (min(list1) > m) and i == 0:
        print(0)
        return
    if sum + min(list1) <= m:
        sum += min(list1)

        list2.append(list1.index(min(list1))+1)
        list1[list1.index(min(list1))] = 999999999999
print(len(list2))
print(' '.join(map(str, list2)))
