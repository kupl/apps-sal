def app(s, alph):
    nonlocal cnt
    alph[s] = cnt
    cnt += 1
def f(s, n, step, alph, used):
    if n == step:
        app(s, alph)
    else:
        if not used[step][0]:
            used[step][0] = True
            f(s + '4', n, step + 1, alph, used)
        if not used[step][1]:
            used[step][1] = True
            f(s + '7', n, step + 1, alph, used)
        used[step][0] = False
        used[step][1] = False
    return
def main():
    nonlocal cnt
    s = input()
    alph = dict()
    string = ''
    for i in range(10):
        used = [[False, False] for i in range(i + 1)]
        f('', i + 1, 0, alph, used)
    print(alph[s])
cnt = 1
main()
