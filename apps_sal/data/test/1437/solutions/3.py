import string
MOD = 1000000007
s = input()
convertion = string.digits + string.ascii_uppercase + string.ascii_lowercase + '-_'
cnt = [0] * 64
for val in range(64):
    for x in range(64):
        for y in range(64):
            if x & y == val:
                cnt[val] += 1
ans = 1
for c in s:
    ans *= cnt[convertion.find(c)]
    ans %= MOD
print(ans)
