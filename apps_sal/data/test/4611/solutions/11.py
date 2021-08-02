N = int(input())
txy = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]

check = True
for i in range(1, N + 1):
    K = txy[i][0] - txy[i - 1][0]
    tmp = K - abs(sum(txy[i][1:]) - sum(txy[i - 1][1:]))
    if tmp < 0 or tmp % 2 == 1:
        check = False
        break

print("Yes" if check else "No")
