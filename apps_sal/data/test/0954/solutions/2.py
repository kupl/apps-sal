s = input()
n = len(s)
S = {s}
for i in range(n):
    s = s[-1] + s[:-1]
    S.add(s)
print(len(S))

