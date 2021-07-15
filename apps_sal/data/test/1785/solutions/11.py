n = int(input())
s = str(input()).upper()
probability_max = 0
Max = 0
modulo = 1000000007
base_acids = [0] * 4
for i in range(n):
    if s[i] == 'A': base_acids[0] += 1
    if s[i] == 'C': base_acids[1] += 1
    if s[i] == 'G': base_acids[2] += 1
    if s[i] == 'T': base_acids[3] += 1
kol = base_acids.count(max(base_acids))
print(kol ** n % modulo)

