n, p = map(int, input().split())
p -= 1
s = input()
if p >= n // 2:
    p = n - 1 - p
l = 0
r = n // 2 - 1

while l < n // 2 and (s[l] == s[n - 1 - l]):
    l += 1
while r >= 0 and (s[r] == s[n - 1 - r]):
    r -= 1
ans, ch = 0, 0
for i in range(l, r + 1):
    temp = abs(ord(s[i]) - ord(s[n - 1 - i]))
    ch += min(temp, 26 - temp)
    #print (min(temp, 26-temp),s[i], s[n-1-i])
if l < r:
    #print (min(abs(p-r), abs(p-l))+ abs(r-l) + ch)
    ans += min(abs(p - r), abs(p - l)) + abs(r - l) + ch
elif l == r:
    if ch:
        ans += abs(p - l) + ch
print(ans)
