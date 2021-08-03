n = int(input())


def inter(n):
    s = str(n)
    cnt = 0
    for i in s:
        cnt += int(i)
    if cnt % 4:
        return False
    return True


while not inter(n):
    n += 1
print(n)
