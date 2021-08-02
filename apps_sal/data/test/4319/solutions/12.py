# import sys
# sys.stdin=open('F:\\C\\Script\\input.txt','r')
# sys.stdout=open('F:\\C\\Script\\output.txt','w')
# sys.stdout.flush()

I = lambda: [int(i) for i in input().split()]

n, = I()
l = I() + [1]
a = []
for i in range(n):
    if l[i + 1] == 1:
        a.append(l[i])
print(l.count(1) - 1)
print(*a)
