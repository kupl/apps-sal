def main():
    n = int(input())
    if n % 4 != 0:
        return 0
    s = input()
    d = dict()
    d['A'] = 0
    d['C'] = 0
    d['G'] = 0
    d['T'] = 0
    for i in s:
        if i in 'ACGT':
            d[i] += 1
    app = ''
    for i in list(d.items()):
        if i[1] <= n // 4:
            app += i[0] * (n // 4 - i[1])
        else:
            return 0
    print(s.replace('?', '{}').format(*list(app)))
    return 1


if not main():
    print('===')
