n = int(input())

ops = input()

l = ops.count('L')
r = ops.count('R')
u = ops.count('U')
d = ops.count('D')

print(min(l,r)*2+min(u,d)*2)
