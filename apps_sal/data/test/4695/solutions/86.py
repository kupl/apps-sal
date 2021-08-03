r = list(map(int, input().split()))
a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
c = [2]
if r[0] == 2 or r[0] == 2:
    print('No')
elif len(list(set(r) & set(a))) == 2:
    print('Yes')
elif len(list(set(r) & set(b))) == 2:
    print('Yes')
else:
    print('No')
