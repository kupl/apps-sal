num = int(input())
numleft = num % 3
out = 2 * (num // 3)
if numleft == 0:
    print(out)
else:
    print(out + 1)
