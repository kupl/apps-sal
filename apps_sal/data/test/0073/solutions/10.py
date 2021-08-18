c, v1, v2, a, l = map(int, input().split())
read = 0
res = 0
vc = v1
while read < c:
    back = min(read, l)
    read += vc - back
    vc = min(vc + a, v2)
    res += 1
print(res)
