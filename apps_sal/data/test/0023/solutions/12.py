from copy import copy


def check(a, b):
    a = int(''.join(sorted(a)))
    b = int(b[1:])

    return a <= b


def get(a, b):
    nonlocal ans
    nonlocal ret

    if a == b:
        ans += list(a)

        ret = True

        return ans

    a = list(a)

    if a == list():
        ret = True

        return ans

    temp = [el for el in a if int(el) <= int(b[0])]
    m = max(temp)

    c = copy(a)
    c.remove(m)

    if m == b[0]:
        if check(c, b):
            ans.append(m)

            get(''.join(c), b[1:])

            if ret:
                return ans

        else:
            while m in temp:
                temp.remove(m)

            m = max(temp)

            d = copy(a)
            d.remove(m)

            ans.append(m)

            ans += sorted(d, reverse=True)

            ret = True

            return ans

    else:
        ans.append(m)

        ans += sorted(c, reverse=True)

        ret = True

        return ans


a = input()
b = input()

ans = list()
ret = False

if len(a) < len(b):
    print(''.join(sorted(a, reverse=True)))

else:  # len(a) == len(b)
    if a == b:
        print(a)
    else:
        print(int(''.join(get(a, b))))

