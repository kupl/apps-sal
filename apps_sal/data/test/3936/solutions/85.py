n = int(input())
s1 = input()
s2 = input()
cnt = []
cnt2 = 0
for i in range(n):
    if cnt2 >= n:
        break
    if s1[cnt2] == s2[cnt2]:
        cnt2 += 1
        cnt.append(1)
    else:
        cnt2 += 2
        cnt.append(2)
if cnt[0] == 1:
    ans = 3
else:
    ans = 6
mod = 10 ** 9 + 7
for i in range(1, len(cnt)):
    if cnt[i - 1] == 1:
        ans *= 2
    elif cnt[i - 1] == 2 and cnt[i] == 2:
        ans *= 3
    ans %= mod
print(ans)
