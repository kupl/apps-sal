def myf(s, m):
    if (s == m):
        return (-1)
    else:
        return (max(len(s), len(m)))


s = input()
m = input()
res = myf(s, m)
print(res)
