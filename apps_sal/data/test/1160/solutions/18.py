def distribution(available, wish):
    double_keys = ['S,M', 'M,L', 'L,XL', 'XL,XXL', 'XXL,XXXL']
    double = {key: [] for key in double_keys}
    people = [''] * len(wish)
    for i, w in enumerate(wish):
        if w.count(',') == 0:
            if available[w] > 0:
                available[w] -= 1
                people[i] = w
            else:
                return ['NO']
        else:
            double[w].append(i)

    for key in double_keys:
        for p in double[key]:
            lack = True
            for size in key.split(','):
                if available[size] > 0:
                    available[size] -= 1
                    people[p] = size
                    lack = False
                    break
            if lack:
                return ['NO']
    return ['YES', people]

def stock():
    return {size: amount for size, amount in zip(['S', 'M', 'L', 'XL', 'XXL', 'XXXL'], map(int, input().split()))}

def request():
    return [input() for i in range(int(input()))]

def solution(n):
    return [input() for i in range(n)]

def answer():
    ans = distribution(stock(), request())
    if ans[0] == 'YES':
        print('YES')
        for p in ans[1]:
            print(p)
    else:
        print('NO')

def check(s, l):
    for size in l:
        if size not in s:
            return False
        else:
            s[size] -= 1
            if s[size] < 0:
                return False
    return True

def compare():
    s = stock()
    r = request()
    ans = distribution(s.copy(), r)
    try:
        usr = input()
        if usr == 'YES':
            l = solution(len(r))
        elif usr == 'NO':
            l = []
        else:
            print(0)
            print('Нарушен формат вывода')
            return
    except EOFError:
        print(0)
        print('Нарушен формат вывода')
        return

    if usr != ans[0] or ans[0] == 'YES' and not check(s.copy(), l):
        print(0)
        print('Failed. T-shirts:', s, '. Request:', ';'.join(r), '. Your solution:', usr, ' - ', ';'.join(l))
    else:
        print(1)
        print('Ok')

answer()
