
def nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def nok(a, b):
    return a * b // nod(a, b)

n, k = list(map(int, input().split()))
print(nok(n, 10 ** k))

