s = input()
K = int(input())
N = len(s)

ans = []

for i in range(min(K, N)):
    for j in range(N - i):
        ans.append(s[j:j + i + 1])

ans.sort()
count = 0
now = '0'
for i in range(len(ans)):
    if ans[i] != now:
        count += 1
        now = ans[i]
        if count == K:
            print(now)
            return
