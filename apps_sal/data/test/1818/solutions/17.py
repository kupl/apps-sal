n = int(input())
a = list(map(int, input().split()))


def f(n):
    return (sum([1 for i in n if i == '1']))


cnt = {}

for i in range(n):
    tmp = f(bin(a[i])[2:])
    if tmp not in cnt:
        cnt[tmp] = 1
    else:
        cnt[tmp] += 1

#print( cnt )

ans = 0
for i in cnt:
    ans += int(cnt[i] * (cnt[i] - 1) / 2)

print(ans)
