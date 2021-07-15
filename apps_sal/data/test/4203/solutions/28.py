S = input()
ans = 0

if S[0] == 'A':
    ans += 1

cnt = 0
for i in range(2, len(S)-1):
    if S[i] == 'C':
        cnt += 1
if cnt == 1:
    ans += 1

cnt = 0
for i in range(len(S)):
    if S[i].isupper():
        cnt += 1
if cnt == 2:
    ans += 1

if ans == 3:
    print('AC')
else:
    print('WA')

