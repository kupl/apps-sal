input()
dictionary = {}
for element in map(int, input().split()):
    if element not in dictionary:
        dictionary[element] = 1
    else:
        dictionary[element] += 1
answer = []
for number in sorted(dictionary.keys(), reverse=True):
    while dictionary[number] > 0:
        answer.append(number)
        for key in answer:
            num = number
            while num:
                (key, num) = (num, key % num)
            dictionary[key] -= 2
        dictionary[number] += 1
print(' '.join(map(str, answer)))
