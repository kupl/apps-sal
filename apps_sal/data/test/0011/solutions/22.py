def nod(a, b):
    if a * b > 0:
        return nod(b, a % b)
    else:
        return a + b


n, a, b, p, q = (int(i) for i in input().split())
print(n // a * p + n // b * q - n // (a * b // nod(a, b)) * min(p, q))
