def main():
    (n, k) = list(map(int, input().split()))
    aa = []
    for i in range(n + 1):
        s = input()
        aa.append(None if s == '?' else int(s))
    qm_cnt = aa.count(None)
    if k:
        if qm_cnt:
            print('Yes' if n & 1 else 'No')
        else:
            x = 0
            for a in reversed(aa):
                x = (x * k + a) % 999999937
            print('No' if x else 'Yes')
    else:
        print('Yes' if aa[0] is None and (not n - qm_cnt & 1) or aa[0] == 0 else 'No')


def __starting_point():
    main()


__starting_point()
