mod_by = 10 ** 9 + 7
n = int(input())
s = input()
a = s.count('A')
c = s.count('C')
g = s.count('G')
t = s.count('T')
m = max(a, c, g, t)
ct = [a, c, g, t].count(m)
print(pow(ct, n, mod_by))
