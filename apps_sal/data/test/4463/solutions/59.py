s = str(input())
t = str(input())


def num2alpha(c):
    return chr(c + 96)


def alpha2num(c):
    return ord(c) - ord('a') + 1


S = [0] * 26
T = [0] * 26
for i in range(len(s)):
    S[alpha2num(s[i]) - 1] += 1
for i in range(len(t)):
    T[alpha2num(t[i]) - 1] += 1
ss = 0
while S[ss] == 0:
    ss += 1
tt = 25
while T[tt] == 0:
    tt -= 1
if tt < ss:
    print('No')
elif tt > ss:
    print('Yes')
elif T[tt] == sum(T) and S[ss] == sum(S):
    if sum(T) > sum(S):
        print('Yes')
    else:
        print('No')
else:
    print('No')
