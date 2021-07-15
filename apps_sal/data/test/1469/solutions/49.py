L = int(input())
k = 1
power = 4
while L >= power:
    k += 1
    power *= 2

power = 1
ans = []
for i in range(k):
    ans.append([k-i, k+1-i, 0])
    ans.append([k-i, k+1-i, power])
    power *= 2

N = k+1
l = power
rest = L - l
while rest > 0:
    power = 1
    k = 0
    while rest >= power * 2:
        power *= 2
        k += 1
    ans.append([1, N-k, l])
    l += power
    rest -= power

print(*[N, len(ans)])
for i in ans:
    print(*i)
