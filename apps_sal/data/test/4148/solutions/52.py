N = int(input())
S = input()
s = []
for i in range(len(S)):
    s.append(chr((ord(S[i]) - 65 + N) % 26 + 65))
print(''.join(s))
