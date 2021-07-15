n = int(input())
while (1):
    s = 0
    temp = str(n)
    for x in temp:
        s += int(x)
    if s % 4 == 0:
        print(temp)
        break
    n+=1

