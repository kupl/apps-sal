import math
X = int(input())

ls = []
for i in range(2, math.floor(math.sqrt(X)) + 1):
    for j in range(2, 10):
        if i ** j <= X:
            ls.append(i ** j)

print(max(ls) if ls else 1)
