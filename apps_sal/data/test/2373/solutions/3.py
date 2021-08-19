n = int(input())
p = list(map(int, input().split()))
cnt = 0
mode = 0
for j in range(n):
    if mode == 0:
        if j + 1 == p[j]:
            cnt += 1
            mode = 1
    else:
        mode = 0
print(cnt)
