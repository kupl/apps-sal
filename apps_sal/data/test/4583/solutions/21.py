n = input()
N = [int(i) for i in n]
for i in range(8):
    n = format(i, '03b')
    ans = N[0]
    msg = str(N[0])
    for j in range(3):
        if n[j] == '0':
            ans += N[j + 1]
            msg += '+' + str(N[j + 1])
        else:
            ans -= N[j + 1]
            msg += '-' + str(N[j + 1])
    if ans == 7:
        print(msg + "=7")
        break
