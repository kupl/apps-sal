from copy import deepcopy
n = int(input())
s = [input() for _ in range(n)]
cnt = []

for si in s:
    tmp = [0] * 26
    for i in range(len(si)):
        tmp[ord(si[i]) - 97] += 1
    if cnt == []:
        cnt = deepcopy(tmp)
    else:
        for j in range(26):
            cnt[j] = min(cnt[j], tmp[j])

ans = ''
for i in range(26):
    for j in range(cnt[i]):
        ans += chr(i + 97)
print(ans)
