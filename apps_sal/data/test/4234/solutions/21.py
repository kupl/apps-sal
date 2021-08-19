n = int(input())
s = input()
o = 0
rem = set()
for (i, c) in enumerate(s):
    if (i ^ o) & 1:
        continue
    if i == n - 1:
        rem.add(i)
        break
    if s[i] == s[i + 1]:
        rem.add(i)
        o ^= 1
res = ''.join((s[i] for i in range(n) if i not in rem))
print(len(rem))
print(res)
