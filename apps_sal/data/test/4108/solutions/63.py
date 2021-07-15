s = input()
t = input()

def f(x):
    dic = {}
    for c in x:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    return dic

d1 = f(s)
d2 = f(t)
l1 = [i for i in d1.values()]
l2 = [i for i in d2.values()]
l1.sort()
l2.sort()

if l1 == l2:
    print('Yes')
else:
    print('No')
