import bisect

s = input()
t = input()

alphabet = [[] for _ in range(26)]
n = len(s)
s += s
for i in range(len(s)):
    alphabet[ord(s[i]) - ord("a")].append(i)
    
ans = 0
now = -1
for i in range(len(t)):
    t_i = ord(t[i]) - ord("a")
    j = bisect.bisect_right(alphabet[t_i], now)
    if j == len(alphabet[t_i]):
        print(-1)
        return
    else:
        now = alphabet[t_i][j]
        if now >= n:
            now -= n
            ans += n
            
print(ans + now + 1)
