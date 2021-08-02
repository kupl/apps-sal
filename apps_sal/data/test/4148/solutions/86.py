l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
L = []
n = int(input())
s = input()
for i in range(len(s)):
    L.append(l[(l.index(s[i]) + n) % 26])

L = ''.join(L)
print(L)
