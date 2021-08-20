n = int(input())
ctleft = 0
ctright = 0
for _ in range(n):
    (x, y) = list(map(int, input().split()))
    if x < 0:
        ctleft += 1
    else:
        ctright += 1
print('YNeos'[not (ctright < 2 or ctleft < 2)::2])
