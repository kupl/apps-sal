n, size = map(int, input().split())
li = []
for _ in range(n):
    a, b = map(int, input().split())
    li.append((a, b, a - b))
sum = 0; sum1 = 0
for i in range(n):
    sum += li[i][1]
    sum1 += li[i][0]
if sum > size:
    print(-1)
    return
if(sum1 <= size):
    print(0)
    return
li.sort(key=lambda x: x[2], reverse=True)
dif = sum1 - size
count = 0
for i in range(n):
    if dif <= 0:
        break
    dif -= li[i][2]
    count += 1
print(count)
