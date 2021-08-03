n = int(input())
s = input()

total = 0
for i, x in enumerate(s):
    if x in "02468":
        total += i + 1
print(total)
