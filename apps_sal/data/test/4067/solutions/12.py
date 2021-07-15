n = int(input())
s = list(input())

ave = n // 3

c0, c1, c2 = 0, 0, 0
for c in s:
    if c == '0': c0 += 1
    if c == '1': c1 += 1
    if c == '2': c2 += 1


for check0 in range(len(s)):
    if s[check0] == '1' and c0 < ave and c1 > ave:
        s[check0] = '0'
        c0 += 1
        c1 -= 1
    elif s[check0] == '2' and c0 < ave and c2 > ave:
        s[check0] = '0'
        c0 += 1
        c2 -= 1

for check1 in range(len(s)):
    if s[check1] == '2' and c1 < ave and c2 > ave:
        s[check1] = '1'
        c1 += 1
        c2 -= 1

for check2 in range(len(s) - 1, -1 , -1):
    if s[check2] == '1' and c2 < ave and c1 > ave:
        s[check2] = '2'
        c2 += 1
        c1 -= 1
    elif s[check2] == '0' and c2 < ave and c0 > ave:
        s[check2] = '2'
        c2 += 1
        c0 -= 1

for check1 in range(len(s) - 1, -1 , -1):
    if s[check1] == '0' and c1 < ave and c0 > ave:
        s[check1] = '1'
        c1 += 1
        c0 -= 1
            
print("".join(s))
