n = int(input())
a = list(map(int, input().split()))

cnt = [0] * (10**5 + 1)

for i in a:
    cnt[i] += 1

x_cnt = [0] * (10**5 + 1)
for x in range(1, 10**5):
    tmp = cnt[x - 1] + cnt[x] + cnt[x + 1]
    x_cnt[x] = tmp

print(max(x_cnt))
