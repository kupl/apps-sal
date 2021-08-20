n = int(input())
mylists = []
for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if i < j or i % 2 == 0:
            break
        if i % j == 0:
            cnt += 1
        if cnt == 8:
            mylists.append(i)
        if cnt >= 9:
            mylists.pop()
            break
print(len(mylists))
