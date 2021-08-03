def solve():
    n = int(input())
    if n % 4 != 0:
        print("===")
        return
    want = n // 4
    s = list(input())
    d = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for c in s:
        if c in d:
            d[c] += 1
    for i in range(n):
        if s[i] == '?':
            for key in d:
                if d[key] < want:
                    d[key] += 1
                    s[i] = key
                    break
    for key in d:
        if d[key] != want:
            print("===")
            return
    print(''.join(s))


solve()
