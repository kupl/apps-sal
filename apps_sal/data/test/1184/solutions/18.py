x = input()
list = x.split()
list2 = []
if list[0][1] == '}':
    list2 = []
else:
    list2.append(list[0][1])
i = 1
while i < len(list):
    list2.append(list[i][0])
    i += 1
list3 = []
for item2 in list2:
    if item2 not in list3:
        list3.append(item2)
print(len(list3))
