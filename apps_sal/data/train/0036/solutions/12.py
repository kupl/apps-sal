n = int(input())
pre = []
row = 1
for i in input().split(' '):
    for j in range(int(i)):
        pre.append(row)
    row += 1
m = int(input())
tasty_worms = []
for i in input().split(' '):
    i = int(i)
    print(pre[i - 1])

