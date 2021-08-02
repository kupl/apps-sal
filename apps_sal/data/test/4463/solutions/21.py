s = input()
t = input()
data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
S = [0] * len(s)
T = [0] * len(t)
for i in range(len(s)):
    S[i] = data.index(s[i])
for i in range(len(t)):
    T[i] = data.index(t[i])
S.sort()
T.sort(reverse=True)
if S < T:
    print('Yes')
else:
    print('No')
