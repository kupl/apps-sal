n = int(input())
pre = []
cur = []
for i in range(n):
    pre.append(input())
for i in range(n):
    cur.append(input())
num = 0
for i in range(n):
    if pre[i] in cur:
        cur.remove(pre[i])
    else:
        num += 1
print(num)
