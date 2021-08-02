num = int(input())
line = input().split(" ")
checklis = sorted(line)
if checklis[0] == "0":
    res = 0
else:
    res = 1
    i = 0
    while res <= 1000000000000000000 and i < num:
        res *= int(line[i])
        i += 1

    if res > 1000000000000000000:
        res = -1

print(res)
