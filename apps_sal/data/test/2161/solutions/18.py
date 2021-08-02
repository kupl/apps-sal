n = int(input())
book = {}
book_cool = {}
for i in range(n):
    li = list(input().split())
    if li[0] not in book:
        book[li[0]] = []
    for num in li[2:int(li[1]) + 2]:
        book[li[0]].append(num[::-1])
for name in book:
    t = book[name]
    t.sort()
    book_cool[name] = set()
    tt = book_cool[name]
    for i in range(1, len(t)):
        if t[i].startswith(t[i - 1]):
            pass
        else:
            tt.add(t[i - 1])
    tt.add(t[-1])
print(len(book_cool))
for i in book_cool:
    print(i, len(book_cool[i]), end=' ')
    for j in book_cool[i]:
        print(j[::-1], end=' ')
    print()
