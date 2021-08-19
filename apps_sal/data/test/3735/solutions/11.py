n = input()
if int(n) < 10:
    print(n)
else:
    sa = '9' * (len(n) - 1)
    b = int(n) - int(sa)
    sb = str(b)
    sum = 0
    for i in sa:
        sum += int(i)
    for i in sb:
        sum += int(i)
    print(sum)
