def main():
    from random import sample
    from operator import itemgetter
    e = enumerate
    n, a = open(0)
    n = int(n)
    d = [0] + [-2**64] * n
    for j, (a, i) in e(sorted(sample([(a, i)for i, a in e(map(int, a.split()))], n), key=itemgetter(0), reverse=1)):
        d = [max(t + a * (~i - j + k + n), d[k - 1] + a * abs(~i + k))for k, t in e(d)]
    print(max(d))


main()
