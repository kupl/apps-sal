s = input().strip()
t = input().strip()
count_s = [0] * 100
count_t = [0] * 100
ans1, ans2 = [0, 0]
for i in range(len(t)):
    count_t[ord(t[i]) - ord('A')] += 1
for i in range(len(s)):
    count_s[ord(s[i]) - ord('A')] += 1
for i in range(58):
    Min = min(count_s[i], count_t[i])
    count_s[i] -= Min
    count_t[i] -= Min
    ans1 += Min
for i in range(58):
    Min = min(count_s[i], count_t[(i + 32) % 64])
    count_s[i] -= Min
    count_t[(i + 32) % 64] -= Min
    ans2 += Min
print(ans1, ans2)
"""
print(count_s)
print(count_t)
"""
