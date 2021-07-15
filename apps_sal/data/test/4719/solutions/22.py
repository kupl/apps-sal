n = int(input())
alp = [input() for _ in range(n)]
ans = ''

for i in range(97, 123):
    cnt = 1001001001
    for s in alp:
        cnt = min(cnt, s.count(chr(i)))
    ans += chr(i)*cnt

print(ans)
