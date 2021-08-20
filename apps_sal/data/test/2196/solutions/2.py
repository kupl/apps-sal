input()
now = 0
alc = 0
ans = 0
for v in map(int, input().split()):
    if not alc or now == v:
        if not alc:
            ans += v
        now = v
        alc += 1
    else:
        while alc and now != v:
            ans += not alc & 1
            alc >>= 1
            now += 1
        ans += v - now
        alc += 1
        now = v
else:
    while alc:
        ans += not alc & 1
        alc >>= 1
print(ans)
