a = [i for i in input().split()]
n = int(input())
ans = None
pol = ['v', '<', '^', '>']
if pol[(pol.index(a[1]) + n) % 4] == a[0]:
    ans = 'ccw'
if pol[(pol.index(a[1]) - n) % 4] == a[0]:
    if ans != None:
        ans = 'undefined'
    else:
        ans = 'cw'
print(ans)
