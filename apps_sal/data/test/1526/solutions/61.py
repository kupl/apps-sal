lst = sorted(list(map(int, input().split())))

mval = lst[-1]
sval = sum(lst)
cn = mval + (sval-mval) % 2
n = (cn * 3 - sval) // 2
print(n)


