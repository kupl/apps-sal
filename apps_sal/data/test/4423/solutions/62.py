def mapt(fn, *args):
    return list(map(fn, *args))


def Atom(segment):
    try:
        return int(segment)
    except ValueError:
        try:
            float(segment)
        except ValueError:
            return segment


def Input():
    return mapt(int, input().split(" "))


def main():
    n = int(input())
    data = [mapt(Atom, input().split(" ")) for _ in range(n)]
    for i in range(n):
        data[i].append(i)
    data = sorted(data, key=lambda x: x[1], reverse=True)
    data = sorted(data, key=lambda x: x[0])
    for row in data:
        print(row[2] + 1)


main()
