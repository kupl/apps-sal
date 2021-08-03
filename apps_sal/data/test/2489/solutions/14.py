N = int(input())
A = list(map(int, input().split()))
A.sort()
MAX = 10**6 + 1
cnt = [0] * MAX

for x in A:
    if cnt[x] != 0:
        cnt[x] = 2
    else:
        for i in range(x, MAX, x):
            cnt[i] += 1

ans = 0
for x in A:
    # 2回以上通った数字 (cnt[x]>1) は，その数字より小さい約数が存在する (割り切れる他の数が存在する)。
    if cnt[x] == 1:
        ans += 1

print(ans)
