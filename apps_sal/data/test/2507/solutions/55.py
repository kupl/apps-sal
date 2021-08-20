def main():
    import numpy as np
    (n, k) = list(map(int, input().split()))
    aa = np.array(sorted(list(map(int, input().split()))), dtype=np.int64)
    f = np.array(sorted(list(map(int, input().split())), reverse=True), dtype=np.int64)
    a = 0
    b = 10 ** 12 + 10
    while a + 1 < b:
        med = (a + b) // 2
        if np.sum(np.maximum(aa - med // f, np.zeros(n, dtype=np.int64))) > k:
            a = med + 1
        else:
            b = med
    if a == b:
        print(a)
    elif np.sum(np.maximum(aa - a // f, np.zeros(n, dtype=np.int64))) > k:
        print(b)
    else:
        print(a)


main()
