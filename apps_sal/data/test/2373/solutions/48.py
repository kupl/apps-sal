n = int(input())
p = list(map(int, input().split()))

cnt = 0
last = -2

for i in range(n):
    if p[i] == i + 1:
        if last == i - 1:
            cnt += 0
            last = -2
        else:
            cnt += 1
            last = i
    else:
        last = -2

print(cnt)
