S = input()
S = list(reversed(S))

m = 2019
cnt = [0 for i in range(m)]

len_S = len(S)
x = 1
tot = 0
ans = 0

for i in range(len(S)):
    cnt[tot] += 1
    tot += (ord(S[i]) - ord('0')) * x
    tot %= m
    ans += cnt[tot]
    x = x * 10 % m

print(ans)
