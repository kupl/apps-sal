n = int(input())
s = list(input())
s.append(0)
x = s[0]
tot = ''
for i in range(n):
    if s[i] != x:
        tot += x + s[i]
        x = s[i + 1]
print(n - len(tot))
print(tot)
