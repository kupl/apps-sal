n, y1 = map(int, input().split())
a = list(map(int, input().split()))
m, y2 = map(int, input().split())
b = list(map(int, input().split()))

a_st, b_st = dict(), dict()
osn = 2 ** 30

k_a, k_b = set(), set()
for el in a:
    try:
        a_st[el % osn] += 1

    except KeyError:
        a_st[el % osn] = 1

    finally:
        k_a.add(el % osn)

for el in b:
    try:
        b_st[el % osn] += 1

    except KeyError:
        b_st[el % osn] = 1

    finally:
        k_b.add(el % osn)

ans = 2
for i in range(1, 31)[::-1]:
    temp = 0

    for el in k_a:
        try:
            temp = max(temp, a_st[el] + b_st[(el + osn // 2) % osn])

        except KeyError:
            temp = max(temp, a_st[el])

    for el in k_b:
        try:
            temp = max(temp, b_st[el] + a_st[(el + osn // 2) % osn])

        except KeyError:
            temp = max(temp, b_st[el])

    ans = max(ans, temp)
    osn //= 2

    k_ = set()
    k_add = set()
    for el in k_a:
        if el >= osn:
            try:
                a_st[el - osn] += a_st[el]

            except KeyError:
                a_st[el - osn] = a_st[el]

            finally:
                del a_st[el]
                k_add.add(el - osn)
                k_.add(el)

    for el in k_:
        k_a.remove(el)

    for el in k_add:
        k_a.add(el)

    k_ = set()
    k_add = set()
    for el in k_b:
        if el >= osn:
            try:
                b_st[el - osn] += b_st[el]

            except KeyError:
                b_st[el - osn] = b_st[el]

            finally:
                del b_st[el]
                k_add.add(el - osn)
                k_.add(el)

    for el in k_:
        k_b.remove(el)

    for el in k_add:
        k_b.add(el)

print(ans)
