
a = int(input())
a = list(format(a, '
map=[0, 5, 3, 2, 4, 1]
a=[a[map[i]] for i in range(6)]
a=''.join(a)
print(int(a, 2))
