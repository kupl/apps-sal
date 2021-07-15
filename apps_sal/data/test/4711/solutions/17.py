a, b, c, = list(map(int, input().split()))

ring=[]
ring.append(a)
ring.append(b)
ring.append(c)

ring.sort()
print((ring[0] + ring[1]))

