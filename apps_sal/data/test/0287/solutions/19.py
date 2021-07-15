

def main():
    n, k = list(map(int, list(input().split())))
    _min = 0
    _max = 0
    if k == n or k == 0:
        print(0, 0)
        return
    _min = 1
    if n <= 3 * k:
        _max = n - k
    else:
        _max = k * 2

    print(_min, _max)
main()

