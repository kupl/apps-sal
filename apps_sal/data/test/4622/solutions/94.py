_ = input()
l = [ int(x) for x in input().split() ]
l.sort()

for i in range(len(l)-1):
    if l[i] == l[i+1]:
        print('NO')
        return

print('YES')

