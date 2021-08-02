S = input()

s = []
for i in S:
    s.append(i)

ss = []
i = 0
while i < len(s) - 2:
    ss.append("".join(s[i:i + 3]))
    i += 1

abso = []
for n in ss:
    abso.append(abs(753 - int(n)))

print(min(abso))
