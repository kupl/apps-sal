from collections import Counter
n = int(input())
s = input()

count = Counter(s[1:])
x = count["E"]

temp = x
for i in range(1, n):
    if s[i - 1] == "W":
        x += 1
    if s[i] == "E":
        x -= 1
    temp = min(temp, x)

print(temp)
