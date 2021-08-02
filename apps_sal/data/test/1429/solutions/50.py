n, s = input().split()
n = int(n)

s_l = list(s)
c = 0
for i in range(n - 1):
    d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for j in range(i + 2, n + 1, 2):
        d[s[j - 1]] += 1
        d[s[j - 2]] += 1
        if d['A'] == d['T'] and d['C'] == d['G']:
            c += 1
print(c)
