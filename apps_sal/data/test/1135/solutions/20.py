#!/usr/bin/env python3

n = int(input())

nmod = n % 2

word = input()
result = []
for i, c in enumerate(word):
    if (i % 2) != nmod:
        result = result + [c]
    else:
        result = [c] + result

print("".join(result))

