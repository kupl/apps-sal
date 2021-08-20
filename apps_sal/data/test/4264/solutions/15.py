N = int(input())
cnt = 0
for i in range(1, N + 1):
    if len(str(i)) & 1 == 1:
        cnt += 1
print(cnt)
