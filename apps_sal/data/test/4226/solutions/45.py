animals_and_legs = input()
list = animals_and_legs.split()
animals = int(list[0])
legs = int(list[1])
j = animals
i = 0
something = True
while i <= animals:
    if i * 4 + j * 2 == legs:
        print('Yes')
        something = False
        break
    i = i + 1
    j = j - 1
if something is True:
    print('No')
