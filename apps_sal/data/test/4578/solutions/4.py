import math
e = list(map(int, input().split()))
j = [int(input()) for _ in range(e[0])]
a = sum(j)
count = e[0]
if a == e[1]:
    count += 0
else:
    count += (e[1] - a) // min(j)
print(count)
