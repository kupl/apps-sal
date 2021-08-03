n = int(input())
ls = list(map(int, input().split()))
cnt = 0
max = 0
for i in range(n):
    if ls[i] != 0:
        cnt += 1
        if cnt > max:
            max = cnt
    else:
        cnt = 0
print(max)
