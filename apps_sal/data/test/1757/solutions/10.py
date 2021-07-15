

def main():
    d = fib()
    n = int(input())
    s = ''
    for i in range(n):
        if i + 1 in d:
            s += 'O'
        else:
            s += 'o'
    print(s)

def fib():
    res = {1, 2}
    f1 = 1
    f2 = 2
    while f1 < 1010:
        res.add(f1 + f2)
        f1, f2 = f2, f1 + f2
    return res



main()















