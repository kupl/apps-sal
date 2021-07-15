_, a, b = list(map(int, input().split()))
s = list(map(int, input().split()))
i = iter(sorted(s[1:], reverse=True))
ssum = sum(s[1:])
s0 = s[0]
cnt = 0

while s and (s0 * a) / (ssum + s0) < b:
    ni = next(i)
    ssum -= ni
    cnt += 1

print(cnt)

