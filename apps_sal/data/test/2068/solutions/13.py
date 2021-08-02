def lower(a):
    if 'A' <= a <= "Z":
        return chr(ord(a) + 32)
    else:
        return a


def ToLower(a):
    a = list(a)
    for i in range(len(a)):
        a[i] = lower(a[i])
    return ''.join(a)


def main():
    n = int(input())
    people = ['polycarp']
    res = [1] * (n + 1)
    for i in range(1, n + 1):
        a, b, c = map(ToLower, input().split())
        res[i] = res[people.index(c)] + 1
        people.append(a)
    print(max(res))


main()
