def get_ans(start):
    t = (start - 1) // 4
    ret = t * 16

    if (start - 1) % 4 in (1, 3):
        ret += 7

    return ret

s = input()

seat = int(s[:-1])
p = s[-1]

ans = get_ans(seat)

if p == 'f':
    ans += 0
elif p == 'e':
    ans += 1
elif p == 'd':
    ans += 2
elif p == 'a':
    ans += 3
elif p == 'b':
    ans += 4
elif p == 'c':
    ans += 5
ans += 1

print(ans)

