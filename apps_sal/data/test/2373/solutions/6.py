N = int(input())
p = list(map(int, input().split()))
count = 0
flag = 0
for i in range(N):
    if flag:
        flag = 0
        continue
    if p[i] == i + 1:
        count += 1
        if i < N - 1 and p[i + 1] == i + 2:
            flag = 1
print(count)
