def get_zcy(a):
    s = str(a)
    ln = len(s)
    return a * 10 ** ln + int(s[::-1])


k, p = list(map(int, input().split()))

print(sum([get_zcy(x) for x in range(1, k + 1)]) % p)
