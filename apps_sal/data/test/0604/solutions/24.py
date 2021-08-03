n = int(input())
ai = list(map(int, input().split()))
ai.sort()
last_el = ai[0]
ans = 0
if ai[0] != 0:
    ans = 1
for i in range(1, n):
    if last_el != ai[i] and ai[i] != 0:
        ans += 1
    last_el = ai[i]
print(ans)
