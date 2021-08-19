n = int(input())
P = list(map(int, input().split()))
s = input()
res = sum((P[i] for i in range(n) if s[i] == 'B'))
maxdiff = 0
suma = 0
sumb = 0
for i in range(n):
    if s[i] == 'A':
        suma += P[i]
    else:
        sumb += P[i]
    if suma - sumb > maxdiff:
        maxdiff = suma - sumb
suma = 0
sumb = 0
for i in range(n)[::-1]:
    if s[i] == 'A':
        suma += P[i]
    else:
        sumb += P[i]
    if suma - sumb > maxdiff:
        maxdiff = suma - sumb
print(res + maxdiff)
