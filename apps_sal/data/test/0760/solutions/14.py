s = input()
n = len(s)
k = int(input())
best = 0
if k >= n:
    best = (k + n) // 2 * 2
for st in range(n):
    for ln in range(2, n - st):
        if s[st:st + ln // 2] == s[st + ln // 2:st + ln]:
            best = max(best, ln)

for st1 in range(n):
    if (n + k - st1) % 2 == 0:
        lens = (n + k - st1) // 2
        nlen = lens - k
        st2 = st1 + lens
        if s[st1:(st1 + nlen)] == s[st2:]:
            best = max(best, lens * 2)
print(best)
