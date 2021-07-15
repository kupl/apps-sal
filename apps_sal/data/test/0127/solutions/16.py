import sys

n, f =  list(map(int, sys.stdin.readline().rstrip().split()))

li = []
li2 = []
for i in range(n):
    k, l = list(map(int, sys.stdin.readline().rstrip().split()))
    li.append((k, l))

li = sorted(li, key=lambda x: min(x[0]*2,x[1])-min(x[0],x[1]))

result = 0
for i in range(n):
    if i >= n-f:
        result += min(li[i][0]*2,li[i][1])
    else:
        result += min(li[i][0],li[i][1])



sys.stdout.write(str(result))


