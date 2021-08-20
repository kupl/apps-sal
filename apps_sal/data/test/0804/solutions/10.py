s = input()
k = int(input())
a = []
cou = 0
for i in range(len(s)):
    if s[i] not in a:
        a.append(s[i])
        cou += 1
if k > len(s):
    print('impossible')
else:
    print(max(k - cou, 0))
