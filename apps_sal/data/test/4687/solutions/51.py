(n, k) = list(map(int, input().split()))
li = []
for i in range(n):
    temp = list(map(int, input().split()))
    li.append(temp)
li.sort()
total = 0
for i in range(n):
    if i == n - 1:
        print(li[i][0])
        break
    total += li[i][1]
    if total < k:
        continue
    else:
        print(li[i][0])
        break
