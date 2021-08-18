
a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())


min_ans = 0
kyoyou = a1 * (k1 - 1) + a2 * (k2 - 1)
min_ans = min(a1 + a2, max(n - kyoyou, 0))

li = []
for i in range(a1):
    li.append(k1)
for i in range(a2):
    li.append(k2)
li = sorted(li)
max_ans = 0
for i in range(len(li)):
    if li[i] <= n:
        max_ans += 1
        n = n - li[i]
    else:
        break
print(min_ans, max_ans)
