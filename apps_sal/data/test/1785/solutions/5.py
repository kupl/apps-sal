n = int(input().rstrip())
s = str(input().rstrip())
kol = 0
mx = 0
mas = [0] * 4
for i in range(n):
    if s[i] == 'A':
        mas[0] += 1
    if s[i] == 'C':
        mas[1] += 1
    if s[i] == 'G':
        mas[2] += 1
    if s[i] == 'T':
        mas[3] += 1
mx = max(mas)
kol = mas.count(mx)
print(kol ** n % 1000000007)
