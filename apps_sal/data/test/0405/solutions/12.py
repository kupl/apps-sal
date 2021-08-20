__author__ = 'Think'
n = int(input())
bumpers = input()
total = 0
for i in bumpers:
    if i == '<':
        total += 1
    else:
        break
for i in reversed(bumpers):
    if i == '>':
        total += 1
    else:
        break
print(total)
