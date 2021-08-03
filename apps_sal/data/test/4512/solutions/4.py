s = input()
q = int(input())
T = []
for i in range(4 * len(s) + 10):
    T.append(0)


def create(rt, l, r):
    if(l == r):
        T[rt] = 1 << (ord(s[l - 1]) - 97)
        return
    mid = (l + r) // 2
    create(rt << 1, l, mid)
    create(rt << 1 | 1, mid + 1, r)
    T[rt] = T[rt << 1] | T[rt << 1 | 1]


def update(rt, l, r, pos, now):
    if(l == r):
        T[rt] = 1 << (ord(now) - 97)
        return
    mid = (l + r) // 2
    if(pos <= mid):
        update(rt << 1, l, mid, pos, now)
    else:
        update(rt << 1 | 1, mid + 1, r, pos, now)
    T[rt] = T[rt << 1] | T[rt << 1 | 1]


def cal(rt, l, r, L, R):
    if(l == L and R == r):
        return T[rt]
    mid = (l + r) // 2
    if(R <= mid):
        return cal(rt << 1, l, mid, L, R)
    elif(L > mid):
        return cal(rt << 1 | 1, mid + 1, r, L, R)
    else:
        return cal(rt << 1, l, mid, L, mid) | cal(rt << 1 | 1, mid + 1, r, mid + 1, R)


n = len(s)
create(1, 1, n)

for i in range(q):
    str = input().split()
    if(str[0] == '1'):
        pos = int(str[1])
        update(1, 1, n, pos, str[2])
    else:
        l = int(str[1])
        r = int(str[2])
        res = cal(1, 1, n, l, r)
        ans = 0
        while(res > 0):
            if(res % 2 == 1):
                ans += 1
            res //= 2
        print(ans)
