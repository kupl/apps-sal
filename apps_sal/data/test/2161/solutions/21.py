n = int(input())
book = dict()
for i in range(n):
    phones = []
    inp = [i for i in input().split()]
    name = inp[0]
    phones = [i for i in inp[2:]]
    for ph in phones:
        if not name in book:
            book[name] = [ph]
            continue
        f = True
        for j in range(len(book[name])):
            if len(book[name][j]) <= len(ph) and ph.rfind(book[name][j]) + len(book[name][j]) == len(ph):
                book[name][j] = ph
                break
            elif len(book[name][j]) >= len(ph) and book[name][j].rfind(ph) + len(ph) == len(book[name][j]):
                f = False
        else:
            if f:
                book[name].append(ph)
print(len(book))
for name in book:
    print(name, len(book[name]), end=' ')
    for ph in book[name]:
        print(ph + '', end=' ')
    print()
