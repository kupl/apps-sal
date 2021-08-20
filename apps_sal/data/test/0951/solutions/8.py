k = int(input())
inp = input()
n = []
for val in inp:
    n.append(int(val))
n.sort()
sumval = sum(n)
counter = 0
for val in n:
    if sumval < k:
        sumval += 9 - val
        counter += 1
    else:
        break
print(counter)
