from collections import Counter
n = int(input())
s = [input() for i in range(n)]
sc = [Counter(list(_s)) for _s in s]

ans = ''
for i in range(26):
    cnt = float('inf')
    for _sc in sc:
        cnt = min(cnt, _sc[chr(ord('a') + i)])
    ans += chr(ord('a') + i) * cnt
print(ans)
