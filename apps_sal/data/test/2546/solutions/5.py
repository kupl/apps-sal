def main():
    from array import array
    import sys
    input1 = sys.stdin.readline
    for _ in range(int(input1())):
        n, s = list(map(int, input1().split()))
        n1 = (n + 1) // 2
        z = array('i', (0,))
        ls = z * n
        rs = z * n
        for i in range(n):
            ls[i], rs[i] = list(map(int, input1().split()))
        for l_ in ls:
            s -= l_
        lbs, rbs = 1, 1000000001
        while lbs + 1 < rbs:
            m = (lbs + rbs) // 2
            st = sorted((min(l_, m) for (l_, r) in zip(ls, rs) if r >= m), reverse=True)
            if len(st) >= n1 and m * n1 <= s + sum(st[:n1]):
                lbs = m
            else:
                rbs = m
        sys.stdout.write(f'{lbs}\n')


main()

