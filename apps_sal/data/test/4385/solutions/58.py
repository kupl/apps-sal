import itertools
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())
lst = [a, b, c, d, e]
c = list(itertools.combinations(lst, 2))
for (i, j) in c:
    if j - i > k:
        print(':(')
        break
else:
    print('Yay!')
