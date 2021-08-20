s = input().split(':')
fir = int(s[0])
sec = int(s[1])


def ispal(a, b):
    if len(a) == 1:
        a = '0' + a
    if len(b) == 1:
        b = '0' + b
    if a[::-1] == b:
        return True


ans = 0
while not ispal(str(fir), str(sec)):
    ans += 1
    sec += 1
    if sec == 60:
        sec = 0
        fir += 1
    if fir == 24:
        fir = 0
        sec = 0
print(ans)
