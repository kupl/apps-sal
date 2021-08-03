def lucky(hh, mm):
    if '7' in str(hh):
        return True
    if '7' in str(mm):
        return True
    return False


x = int(input())
h, m = map(int, input().split())
cnt = 0
while not lucky(h, m):
    m -= x
    if m < 0:
        m += 60
        h -= 1
    if h < 0:
        h += 24
    cnt += 1

print(cnt)
