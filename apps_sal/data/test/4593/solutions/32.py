X = int(input())
lst = [1]
for i in range(2, 32):
    for j in range(2, 10):
        x = i ** j
        if x <= 1000:
            lst.append(x)
if X in lst:
    print(X)
else:
    lst.append(X)
    lst2 = sorted(lst)
    n = lst2.index(X)
    print(lst2[n-1])
