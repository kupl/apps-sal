s = input()
n = int(input())
freq = [0 for i in range(0, 300)]
raport = [0 for i in range(0, 300)]
differentLetters = 0
tickets = 0
sol = ''

for c in s:
    freq[ord(c)] += 1
for i in freq:
    if i > 0:
        differentLetters += 1

if differentLetters > n:
    print('-1')
    return

for i in 'abcdefghijklmnopqrstuvwxyz':
    if freq[ord(i)] == 0:
        continue
    sol += i
    freq[ord(i)] -= 1
    raport[ord(i)] = freq[ord(i)]


for i in range(differentLetters, n):
    # pun litera cu cea mai mare frecventa

    maxRaport = raport[ord('z')]
    chosenLetter = 'z'
    for j in 'abcdefghijklmnopqrstuvwxyz':
        if raport[ord(j)] > maxRaport:
            maxRaport = raport[ord(j)]
            chosenLetter = j

    sol += chosenLetter
    raport[ord(chosenLetter)] = freq[ord(chosenLetter)] / sol.count(chosenLetter)


for i in sol:
    a = s.count(i)
    b = sol.count(i)

    if a % b == 0:
        tickets = max(tickets, int(a // b))
    else:
        tickets = max(tickets, int(a // b) + 1)

print(tickets)
print(sol)
