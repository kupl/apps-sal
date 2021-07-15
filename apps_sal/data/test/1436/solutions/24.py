n = int(input())
a = map(int, input().split())
cnt = 0
sum = 0
for i in a:
    if i < 0 and sum <= 0:
        cnt += 1
    elif i > 0:
        sum += i
    elif i < 0 and sum > 0:
        sum += i
print(cnt)
