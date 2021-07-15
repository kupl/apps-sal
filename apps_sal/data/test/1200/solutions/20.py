import fractions
n = int(input())
s = [int(x) for x in input().split()]
s.sort(reverse=True)
nod = abs(s[0] - s[1])
for i in range(1, n):
    delta = abs(s[i] - s[i - 1])
    nod = fractions.gcd(nod, delta)
max_i = s[0]
min_i = s[-1]
print((max_i - min_i) // nod + 1 - n)
