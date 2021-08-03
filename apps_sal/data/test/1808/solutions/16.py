nkx = [int(i) for i in input().split(' ')]
ai = [int(i) for i in input().split(' ')]
k = nkx[1]
x = nkx[2]
ai = ai[:-k] + [x] * k
print(sum(ai))
