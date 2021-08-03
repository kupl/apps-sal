x = int(input())

hh, mm = map(int, input().split())


def ch(hh, mm):
    return '7' in str(hh) or '7' in str(mm)


count = 0
while not ch(hh, mm):
    count += 1
    if mm >= x:
        mm -= x
    else:
        hh -= 1
        mm -= x - 60
    if hh < 0:
        hh = 23
print(count)
