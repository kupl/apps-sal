S = input()
ans = 0
C1 = 0
up = 0
if S[0] == 'A':
    ans += 1
for i in range(2, len(S) - 1):
    if S[i] == 'C':
        C1 += 1
for j in range(len(S)):
    if S[j].isupper() == 1:
        up += 1
if ans == 1 and C1 == 1 and (up == 2):
    print('AC')
else:
    print('WA')
