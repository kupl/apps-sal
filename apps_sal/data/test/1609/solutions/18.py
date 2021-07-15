num = int(input())
list1 = input().split(' ')

inv = set()

for i in list1:
    inv.add(int(i))
    
missing = []
notE = []

for i in range(1,num+1):
    if i not in inv:
        missing.append(i)

written = set()

j = 0

for i in range(len(list1)):
    if list1[i] in written or int(list1[i])>num:
        list1[i] = str(missing[j])
        written.add(list1[i])
        j += 1
    else:
        written.add(list1[i])
        
        
print(*list1)

