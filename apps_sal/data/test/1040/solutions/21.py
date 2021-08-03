import sys

# B - Abbreviate Fox
N = int(input())
s = input()
t = ''

for c in s:
    t += c

    if t.endswith('fox'):
        t = t[:len(t) - 3]

print(len(t))
