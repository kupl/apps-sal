x = input()
pylons = [0]
y = input()
y += ' '
vesl = ''
for letter in y:
    if letter == ' ':
        pylons.append(int(vesl))
        vesl = ''
    else:
        vesl += letter
energy = 0
money = 0
for i in range(len(pylons) - 1):
    if pylons[i + 1] > pylons[i] + energy:
        money += pylons[i + 1] - (pylons[i] + energy)
        energy = 0
    else:
        energy += pylons[i] - pylons[i + 1]
print(money)
