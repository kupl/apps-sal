s = list(input())
t = list(input())
cnt1 = [[] for _ in range(26)]
cnt2 = [[] for _ in range(26)]
for i in range(len(s)):
    num1 = ord(s[i]) - 97
    num2 = ord(t[i]) - 97
    if t[i] not in cnt1[num1]:
        cnt1[num1].append(t[i])
    if s[i] not in cnt2[num2]:
        cnt2[num2].append(s[i])
ans = 0
for i in range(26):
    if len(cnt1[i]) > 1:
        ans = 1
        break
    if len(cnt2[i]) > 1:
        ans = 1
        break
if ans == 0:
    print('Yes')
else:
    print('No')
