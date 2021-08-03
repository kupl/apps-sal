phones = dict()
n = int(input())

for i in range(n):
    name, num, *numbers = input().split()
    for number in numbers:
        try:
            for el in phones[name]:
                if el.endswith(number):
                    break
                if number.endswith(el):
                    phones[name].remove(el)
                    phones[name].add(number)
                    break
            else:
                phones[name].add(number)
        except KeyError:
            phones[name] = {number}

print(len(phones))
print('\n'.join([' '.join([name, ' '.join([str(len(numbers)), ' '.join(numbers)])]) for name, numbers in list(phones.items())]))
