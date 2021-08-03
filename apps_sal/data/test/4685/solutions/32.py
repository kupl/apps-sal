l = list(map(int, input().split()))
k = int(input())

d = max(l)
e = d * (2**k)

l.remove(max(l))
l.append(e)

print((sum(l)))
