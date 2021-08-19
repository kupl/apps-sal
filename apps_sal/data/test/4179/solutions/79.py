(N, M, C) = map(int, input().split())
base_list = list(map(int, input().split()))
multi = 0
ans = 0
for i in range(N):
    second_list = list(map(int, input().split()))
    for j in range(M):
        multi += base_list[j] * second_list[j]
    if multi + C > 0:
        ans += 1
        multi = 0
    else:
        multi = 0
print(ans)
