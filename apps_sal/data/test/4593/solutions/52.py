x = int(input())
table = [False] * -~x
table[1] = True
for i in range(2, 32):
    j = i * i
    while j <= x:
        table[j] = True
        j *= i
print(max((i for i in range(x + 1) if table[i])))
