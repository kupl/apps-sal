n, k = map(int, input().split())
a = map(int, input().split())

cs = list(range(1, n+1))
l = 0
res = ""
len = n

for x in a:
    pos = (l + x) % len
    #print(cs, pos)
    res += str(cs[pos]) + " "
    del cs[pos]
    len -= 1
    l = pos

print(res)
