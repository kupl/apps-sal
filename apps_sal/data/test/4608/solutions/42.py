n = int(input())
li = [0]
for i in range(n):
    li.append(int(input()))

count = 0
now = 1
while now != 2:
    if li[now] == 0:
        count = -1
        break
    else:
        a = li[now]
        li[now] = 0
        now = a
        count += 1

print(count)
