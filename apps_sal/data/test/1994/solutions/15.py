s = input()
n = len(s)
if n == 1:
    print(1)
    print(1, 1)
    quit()
priya = [-1] * n
q = -1
for i in range(1, n):
    while q >= 0 and s[i] != s[q + 1]:
        q = priya[q]
    if s[i] == s[q + 1]:
        q += 1
        priya[i] = q
cnt = [1] * n
for i in range(n - 1, -1, -1):
    if priya[i] >= 0:
        cnt[priya[i]] += cnt[i]
Ans = [(n, 1)]
q = priya[n - 1]
while q >= 0:
    Ans.append((q + 1, cnt[q]))
    q = priya[q]
Ans.sort()
print(len(Ans))
for i in Ans:
    print(*i)
