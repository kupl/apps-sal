N = int(input())
S1 = input()
S2 = input()

m1 = ""
m = 10**9 + 7
S1 += "."
for i in range(len(S1) - 1):
    if S1[i] == S1[i + 1]:
        m1 += 'y'
    else:
        m1 += 't'
m1 = m1.replace('yt', 'y')
score = [1] * len(m1)
for i in range(1, len(m1)):
    if m1[i - 1] == 't' and m1[i] == 't':
        score[i] = 2
    elif m1[i - 1] == 'y' and m1[i] == 't':
        score[i] = 1
    elif m1[i - 1] == 't' and m1[i] == 'y':
        score[i] = 2
    elif m1[i - 1] == 'y' and m1[i] == 'y':
        score[i] = 3
if m1[0] == 'y':
    score[0] = 6
else:
    score[0] = 3

ans = 1
for i in range(len(m1)):
    ans = (ans * score[i]) % m
print(ans)
