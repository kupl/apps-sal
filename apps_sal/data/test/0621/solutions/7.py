n = int(input())
l = list(map(int, input().split()))
folders = [0]
cur = 0
loss = 0
for i in range(n):
    if l[i] < 0:
        loss += 1
        if loss == 3:
            folders.append(0)
            loss = 1
            cur += 1
    folders[cur] += 1
print(len(folders))
print(*folders)
