
ptr = ord('a')


def s_has_smaller(s_cnt_local, c):
    nonlocal ptr
    for i in range(ptr, ord(c)):
        ptr = i
        if s_cnt_local[i] > 0:
            return True
    return False


s = list(input())
s.reverse()


t = []
u = []

s_cnt = [0] * (ord('z') + 1)
for x in s:
    s_cnt[ord(x)] += 1


while s or t:
    # print('+'*10)
    # print(s)
    # print(t)
    # print(u)
    # print(s_cnt)
    # print(t_cnt)
    if not s:
        while t:
            u.append(t.pop())
    elif not t:
        x = s.pop()
        s_cnt[ord(x)] -= 1
        t.append(x)
    else:
        if s_has_smaller(s_cnt, t[-1]):
            x = s.pop()
            s_cnt[ord(x)] -= 1
            t.append(x)
        else:
            x = t.pop()
            u.append(x)

print("".join(u))
