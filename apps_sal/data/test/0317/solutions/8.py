rng = int(input())
instr = list(input().lower())

chars = []
for i in range(26):
    chars.append(0)

for char in range(rng):
    chars[ord(instr[char])-97] += 1

isyes = True
for i in range(26):
    if chars[i] == 0:
        print('NO')
        isyes = False
        break

if isyes:
    print('YES')

