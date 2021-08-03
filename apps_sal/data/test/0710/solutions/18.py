n = int(input())
s = input()
genome = 'ACTG'


def cnt(a, b):
    a, b = ord(a) - 65, ord(b) - 65
    return min(abs(b - a), 26 - abs(b - a))


mn = 1 << 30
for i in range(n - 3):
    mn = min(mn, sum([cnt(s[i + j], genome[j]) for j in range(4)]))
print(mn)
