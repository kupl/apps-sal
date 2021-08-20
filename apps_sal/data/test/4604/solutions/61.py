n = int(input())
A = list(map(int, input().split()))
d = {}
for a in A:
    d[a] = d.get(a, 0) + 1
zero_cnt = 0
two = 0
no = 0
for i in d:
    if i == 0:
        zero_cnt += 1
    elif d[i] == 2:
        two += 1
    else:
        no += 1
if no != 0 or (n % 2 == 0 and zero_cnt != 0) or (n % 2 == 1 and zero_cnt != 1):
    print(0)
else:
    ans = 1
    mod = 10 ** 9 + 7
    for i in range(two):
        ans *= 2
        ans %= mod
    print(ans % mod)
