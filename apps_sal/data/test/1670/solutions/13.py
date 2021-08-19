h = input()
a = input()
n = int(input())
dic = {}
while n > 0:
    n -= 1
    line = input().split()
    t = line[0]
    m = 0
    if line[1].startswith('a'):
        m += 100
    m += int(line[2])
    f = 1
    if line[3].startswith('r'):
        f += 1
    give_red = False
    if m in list(dic.keys()):
        if dic[m] < 2:
            give_red = True
        dic[m] += f
    else:
        dic[m] = f
        if f > 1:
            give_red = True
    if give_red:
        line = ' ' + t
        if m > 100:
            line = a + ' ' + str(m - 100) + line
        else:
            line = h + ' ' + str(m) + line
        print(line)
