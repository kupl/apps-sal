N = int(input())
cnt = 0

for i in range((N // 4) + 1):
    for j in range((N // 7) + 1):
        if 4 * i + 7 * j == N:
            cnt += 1
if cnt > 0:
    print("Yes")
else:
    print("No")
