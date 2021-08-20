def some(num):
    return '+' if num == 0 else '-'


def main():
    (a, b, c, d) = map(int, input())
    for i in range(2):
        for j in range(2):
            for v in range(2):
                op1 = some(i)
                op2 = some(j)
                op3 = some(v)
                if eval(f'a{op1}b{op2}c{op3}d') == 7:
                    print(f'{a}{op1}{b}{op2}{c}{op3}{d}=7')
                    return


main()
