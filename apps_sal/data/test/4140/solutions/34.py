s = input()

start = ['0', '1']
ans = 10**6
for offset in [0,1]:
    now = 0
    for i in range(len(s)):
        j = (i+offset) % 2
        if s[i] != start[j]:
            now += 1
    ans = min(ans, now)

print(ans)

