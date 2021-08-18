n = int(input())
s = input()

sd = 0
qd = 0

for i in range(n // 2):
    if s[i] == '?':
        qd += 1
    else:
        sd += int(s[i])

    if s[n // 2 + i] == '?':
        qd -= 1
    else:
        sd -= int(s[n // 2 + i])

if abs(sd) % 9 > 0:
    print("Monocarp")
    return

if sd >= 0:
    qd += 2 * (sd // 9 + (1 if sd % 9 > 0 else 0))
else:
    sd = -1 * sd
    qd -= 2 * (sd // 9 + (1 if sd % 9 > 0 else 0))

print("Bicarp" if qd == 0 else "Monocarp")
