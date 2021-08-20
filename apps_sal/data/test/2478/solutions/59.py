n = int(input())
s = input()
(R, L) = (0, 0)
for i in range(len(s)):
    if s[i] == '(':
        R += 1
    elif R:
        R -= 1
    else:
        L += 1
print('(' * L + s + ')' * R)
