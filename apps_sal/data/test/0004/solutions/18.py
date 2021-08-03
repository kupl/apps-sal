x = int(input())
h, m = list(map(int, input().split()))
t = 60 * h + m


def check(t):
    h = str(t // 60)
    m = str(t % 60)
    if '7' in h + m:
        return True
    return False


an = 0
while not check(t):
    t -= x
    an += 1
    if t < 0:
        t = 24 * 60 + t
print(an)
