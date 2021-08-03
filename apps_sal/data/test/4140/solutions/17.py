s = input()
s1 = []
s2 = []
ans1 = 0
ans2 = 0
for i in range(len(s)):
    if i % 2 != 0:
        s1.append('0')
    else:
        s1.append('1')
for i in range(len(s)):
    if i % 2 == 0:
        s2.append('0')
    else:
        s2.append('1')

for x, y in zip(s, s1):
    if x != y:
        ans1 += 1
for x, y in zip(s, s2):
    if x != y:
        ans2 += 1

print(min(ans1, ans2))
