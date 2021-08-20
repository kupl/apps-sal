num = int(input())
a = []
for i in range(num):
    n = int(input())
    a.append(n)
myset = set(a)
len_list = len(frozenset(myset))
print(len_list)
