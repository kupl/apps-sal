from sys import stdin

n = int(stdin.readline())

s = stdin.readline().strip().split('W')

s = [block for block in s if block != '']

print(len(s))

for block in s:
    print(len(block), end=' ')
if s:
    print()

