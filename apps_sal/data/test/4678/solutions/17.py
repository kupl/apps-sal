n = input()
x = [int(i) for i in input().split()]

tmp = x[0]
tot = 0


for i in x:
    if i <= tmp:
        tot += tmp - i
    else:
        tmp = i


print(f"{tot}")
