lst = input()
lst = lst.split()
for i in range(len(lst)):
    lst[i] = int(lst[i])
if lst[0] >= 13:
    print(lst[1])
elif lst[0] < 6:
    print(0)
else:
    print(int(lst[1] / 2))
