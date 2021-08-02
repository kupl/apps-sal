import itertools
import math
n = int(input())
word = [input() for _ in range(n)]
count = 0


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


for i in range(n):
    word[i] = sorted(word[i])

new_word = list(sorted(word))

x = 1

for i in range(n - 1):
    if new_word[i] == new_word[i + 1]:
        x += 1
    elif x >= 2:
        count += combinations_count(x, 2)
        x = 1
if x >= 2:
    count += combinations_count(x, 2)

print(count)
