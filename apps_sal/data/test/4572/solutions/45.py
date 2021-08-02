s = str(input())
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in s:
    if i in L:
        L.remove(i)
if L == []:
    print('None')
else:
    print(L[0])
