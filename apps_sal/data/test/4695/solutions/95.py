(a, b) = input().split()
a = int(a)
b = int(b)
l1 = [1, 3, 5, 7, 8, 10, 12]
l2 = [4, 6, 9, 11]
if a in l1 and b in l1:
    print('Yes')
elif a in l2 and b in l2:
    print('Yes')
else:
    print('No')
