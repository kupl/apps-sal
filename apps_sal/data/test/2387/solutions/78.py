from sys import stdin

def main():
    plus, minus = [], []
    readline = stdin.readline
    n = int(readline())
    for _ in range(n):
        s = readline().rstrip()
        if 2 * s.count('(') - len(s) > 0:
            plus.append(s)
        else:
            minus.append(s)
    plus.sort(key = lambda x: x.count(')'))
    minus.sort(key = lambda x: x.count('('), reverse = True)

    sum = 0
    for v in ''.join(plus + minus):
        sum = sum + (1 if v == '(' else -1)
        if sum < 0 : return print('No')
    if sum != 0:
        return print('No')

    return print('Yes')

def __starting_point():
    main()

__starting_point()
