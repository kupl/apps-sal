from collections import Counter
S = reversed(input())
residuelist = [0]
power = 1
residue = 0
for i in S:
    digit = int(i)
    residue = (residue + power * digit) % 2019
    residuelist.append(residue)
    power = (power * 10) % 2019
val = Counter(residuelist).values()
ans = 0
for j in val:
    ans += j * (j - 1) // 2
print(ans)
