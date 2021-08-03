n = int(input())
a = [int(i) for i in input().split(" ")]
was_one = False
res = sum(a)
zeros = 0
for i in a:
    if (i == 1):
        was_one = True
        if (zeros == 1):
            res += 1
        zeros = 0
    if (was_one and i == 0):
        zeros += 1
print(res)
