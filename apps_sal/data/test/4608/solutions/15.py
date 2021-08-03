N = int(input())

lst = []
for i in range(N):
    lst.append(int(input()))

now = 1
count = 0

for i in range(N):
    now = lst[now - 1]
    count += 1
    if now == 2:
        print(count)
        return

print(-1)
