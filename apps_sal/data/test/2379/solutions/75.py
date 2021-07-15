def main():
    n, k, c = (int(i) for i in input().split())
    s = input()

    if k > sum(1 for c in s if c == 'o'):
        return

    latest = [None] * k
    earliest = [None] * k
    earliest[0] = s.index('o')
    for i in range(1, k):
        try:
            earliest[i] = s.index('o', earliest[i-1] + c + 1)
        except ValueError:
            return
    
    latest[-1] = s.rindex('o')
    for i in reversed(list(range(k-1))):
        try:
            latest[i] = s.rindex('o', 0, latest[i+1] - c)
        except ValueError:
            return

    bound_days = [earliest[i] + 1 for i in range(k) if earliest[i] ==
            latest[i]]

    for e, l in zip(earliest, latest):
        if e == l:
            print((e + 1))
main()

