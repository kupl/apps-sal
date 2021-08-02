N = int(input())
listy = input()
count = 0
for x in listy:
    if x == '<':
        count += 1
    else:
        break
for x in listy[::-1]:
    if x == '>':
        count += 1
    else:
        break

print(count)
