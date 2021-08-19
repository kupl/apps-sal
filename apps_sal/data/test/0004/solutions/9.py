def read():
    return list(map(int, input().split()))


x = int(input())
(hh, mm) = read()
r = 0
while '7' not in str(mm) and '7' not in str(hh):
    mm -= x
    if mm < 0:
        hh -= 1
        mm += 60
    if hh < 0:
        hh = 23
    r += 1
print(r)
