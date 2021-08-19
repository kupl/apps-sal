n = int(input())
ku = input()
si = input()
ka = input()


def bu2num(bu):
    dif = ord(bu) - ord('a')
    if dif >= 0 and dif < 26:
        return dif
    else:
        return ord(bu) - ord('A') + 26


def num2bu(num):
    return chr(ord('a') + num if num < 26 else ord('a') + num - 26)


def bus(s):
    x = [0] * 26 * 2
    for bu in s:
        x[bu2num(bu)] += 1
    return x


def mabus(arr):
    max = 0
    for a in arr:
        if a > max:
            max = a
    return max


def calc(s):
    l = len(s)
    m = mabus(bus(s))
    d = m + n
    if m == l and n == 1:
        return l - 1
    elif d <= l:
        return d
    else:
        return l


kun = calc(ku)
sin = calc(si)
kan = calc(ka)
if kun > sin and kun > kan:
    print('Kuro')
elif sin > kun and sin > kan:
    print('Shiro')
elif kan > kun and kan > sin:
    print('Katie')
else:
    print('Draw')
