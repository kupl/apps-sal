(a, b) = map(str, input().split())
list = []


def Repetition(x: str, y: str):
    list.append(x * int(y))
    return


Repetition(a, b)
Repetition(b, a)
list.sort()
print(list[0])
