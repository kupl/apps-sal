S = str(input())
s = list(map(str, S))
N = len(s)
t = 0
for i in range(int((N-1)/2)):
    if s[i] != s[N-i-1]:
        t += 1
        break
for i in range(int((N-1)/4)):
    if s[i] != s[int((N-1)/2) - i - 1]:
        t += 1
        break

if t == 0:
    print('Yes')
else:
    print('No')
