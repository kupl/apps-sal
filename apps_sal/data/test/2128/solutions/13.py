def solve():
    s = input()
    if 'aa' in s or 'bb' in s or 'cc' in s:
        print(-1)
        return
    syms = s + '@'
    ans = ['@']
    for i, sym in enumerate(s):
        if sym != '?':
            ans.append(sym)
            continue
        for x in 'abc':
            if x != ans[-1] and x != syms[i + 1]:
                ans.append(x)
                break
    print(''.join(ans[1:]))


def solveb():
    n = int(input())
    perm = [int(x) for x in input().split()]
    num___idx = [-1 for _ in range(n + 1)]
    for i, num in enumerate(perm):
        num___idx[num] = i

    curr_max = -1
    curr_min = 2 * n
    num___pretty = [0 for _ in range(n + 1)]
    for num in range(1, n + 1):
        curr_max = max(num___idx[num], curr_max)
        curr_min = min(num___idx[num], curr_min)
        if curr_max - curr_min + 1 == num:
            num___pretty[num] = 1
    print(*num___pretty[1:], sep='')


def solvec():
    n = int(input())
    rank___problems_nr = [int(x) for x in input().split()]
    weird_prefsums = [0]
    last_num = rank___problems_nr[0]
    for num in rank___problems_nr:
        if num != last_num:
            last_num = num
            weird_prefsums.append(weird_prefsums[-1])
        weird_prefsums[-1] += 1

    gold = weird_prefsums[0]
    silvers = 0
    i = 1
    for i in range(1, len(weird_prefsums)):
        x = weird_prefsums[i]
        if x - gold > gold:
            silvers = x - gold
            break

    bronzes = 0
    for j in range(i, len(weird_prefsums)):
        x = weird_prefsums[j]
        if x > n / 2:
            break
        if x - gold - silvers > gold:
            bronzes = x - gold - silvers
    if bronzes == 0 or silvers == 0:
        print(0, 0, 0)
        return

    print(gold, silvers, bronzes)


def solved():
    a, b, c, d = (int(x) for x in input().split())
    ab_len = min(a, b)
    a -= ab_len
    b -= ab_len
    cd_len = min(c, d)
    c -= cd_len
    d -= cd_len

    if a == 1 and cd_len == 0 and d == 0 and c == 0:
        print('YES')
        print('0 1 ' * ab_len + '0')
        return
    if d == 1 and ab_len == 0 and a == 0 and b == 0:
        print('YES')
        print('3 ' + '2 3 ' * cd_len)
        return
    if a > 0 or d > 0:
        print('NO')
        return

    cb_len = min(b, c)
    b -= cb_len
    c -= cb_len
    if b > 1 or c > 1:
        print('NO')
        return
    print('YES')
    print('1 ' * b + '0 1 ' * ab_len + '2 1 ' * cb_len + '2 3 ' * cd_len + '2' * c)


def get_me(prob, mod):
    # return 100, prob
    return (100 * pow(prob, mod - 2, mod)) % mod


def solvee():
    n = int(input())
    mod = 998244353
    idx___prob = [int(x) for x in input().split()]
    curr_me = get_me(idx___prob[0], mod)
    for prob in idx___prob[1:]:
        me = get_me(prob, mod)
        curr_me *= me
        curr_me %= mod

        curr_me += me
        curr_me %= mod

    # curr_q_me = pow(curr_q_me, mod - 2, mod)

    print(curr_me)


def __starting_point():
    solvee()

__starting_point()
