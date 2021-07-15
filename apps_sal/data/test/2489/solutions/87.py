N = int(input())
A_list = list(map(int, input().split()))

yakusu = [0] * (10 ** 6 + 10)
for i in range(N):
    a = A_list[i]
    if yakusu[a] != 0:
        yakusu[a] = 2
        continue
    for j in range(a, 10 ** 6 + 10, a):
        yakusu[j] += 1

ans = 0
for a in A_list:
    if yakusu[a] == 1:
        ans += 1
print(ans)
