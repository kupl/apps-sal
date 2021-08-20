def do(string):
    num = 0
    ok = []
    for i in [12, 6, 4, 3, 2, 1]:
        for j in range(0, i):
            if string[j::i] == 'X' * int(12 / i):
                ok.append(str(int(12 / i)) + 'x' + str(i))
                num += 1
                break
    ok = [str(num)] + ok
    print(' '.join(ok))


for i in range(int(input())):
    do(input())
