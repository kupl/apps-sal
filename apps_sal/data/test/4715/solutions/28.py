A = list(map(int, input().split()))
Num = [0] * 101
cnt = 0
for i in A:
    Num[i] += 1
    if Num[i] == 1:
        cnt += 1
print(cnt)
