
n, Q = list(map(int, input().strip().split()))

s = input()
d = 1

for q in range(Q):
    arr = [0] * (10)

    l, r = list(map(int, input().strip().split()))

    su = ""
    for i in range(l - 1, r):
        su += s[i]
    su = list(su)
    i = 0
    d = 1
    ll = 0
    while i < len(su) and i >= 0:
        if su[i].isdigit():
            arr[int(su[i])] += 1
            if su[i] == '0':
                su = su[:i] + su[i + 1:]
                if d == 1:
                    i -= 1
            else:
                su[i] = str(int(su[i]) - 1)
            if d == 1:
                i += 1
            else:
                i -= 1
            ll = 0
        else:
            if su[i] == '>' or su[i] == '<':

                if d == 1 and i != 0 and ll == 1:
                    if su[i - 1] == '>' or su[i - 1] == '<':
                        su = su[:i - 1] + su[i:]
                        i -= 1
                if d == 0 and i != n - 1 and ll == 1:
                    if su[i + 1] == '>' or su[i + 1] == '<' or su[i + 1] == '-1':
                        su = su[:i + 1] + su[i + 2:]

                if su[i] == '>':
                    d = 1
                else:
                    d = 0
            if d == 0:
                i -= 1
            else:
                i += 1
            ll = 1
    print(*arr)
