N = int(input())
cnt = 0
Ans = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i % j == 0 and i % 2 == 1:
            cnt += 1
    if cnt == 8:
        Ans += 1
    cnt = 0

print(Ans)
