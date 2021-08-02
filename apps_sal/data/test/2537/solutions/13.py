def gns():
    return list(map(int, input().split()))


t = int(input())


def one():
    s = input()
    t = input()
    p = input()
    j = 0
    for c in s:
        while j < len(t) and t[j] != c:
            j += 1
        if j == len(t):
            print('NO')
            return
        j += 1

    def get_num(x):
        ans = [0] * 26
        for c in x:
            c = ord(c) - ord('a')
            ans[c] += 1
        return ans
    ss = get_num(s)
    tt = get_num(t)
    pp = get_num(p)
    for i in range(26):
        if ss[i] + pp[i] < tt[i]:
            print('NO')
            return
    print('YES')


for i in range(t):
    one()
