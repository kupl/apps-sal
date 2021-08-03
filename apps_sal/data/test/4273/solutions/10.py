from itertools import combinations

n = int(input())
s = [input() for _ in range(n)]

letters = {"M": 0, "A": 0, "R": 0, "C": 0, "H": 0, }
to_check = combinations([i for i in "MARCH"], 3)

for word in s:
    if word[0] in letters:
        letters[word[0]] += 1

count = 0
for i in to_check:
    count += letters[i[0]] * letters[i[1]] * letters[i[2]]

print(count)
