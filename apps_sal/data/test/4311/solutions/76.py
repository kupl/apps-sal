s = int(input())

mp = [False] * (10**6 + 1)


def even_f(n):
    return n // 2


def odd_f(n):
    return 3 * n + 1


mp[s] = True
now = s
for i in range(1, 10**6 + 1):
    if(now % 2 == 0):
        now = even_f(now)
    else:
        now = odd_f(now)

    if(mp[now]):
        savei = i
        break
    mp[now] = True

print((savei + 1))
