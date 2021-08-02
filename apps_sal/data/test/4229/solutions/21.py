n = int(input())
cnt = 0
for i in range(1, n + 1):
    if i % 15 == 0:
        cnt += 0
    elif i % 3 == 0:
        cnt += 0
    elif i % 5 == 0:
        cnt += 0
    else:
        cnt += i
print(cnt)
