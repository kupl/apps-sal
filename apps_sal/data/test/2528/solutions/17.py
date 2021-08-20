n = int(input())
a = [int(i) for i in input().split()]
prod = 1
max = 0
c = 0
for i in a:
    if i == 0:
        prod = 1
        c = 0
    else:
        prod = prod * i
        c += 1
        if c > max:
            max = c
print(max)
