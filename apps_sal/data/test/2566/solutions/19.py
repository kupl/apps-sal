from math import ceil


def main():
    k = int(input())
    d = [idx for (idx, di) in enumerate(input().split()) if di == '1']
    dow = len(d)
    w = ceil(k / dow) - 1
    m = k % dow
    ans = [d[(m - 1 + x) % dow] + 7 * (w + int(m - 1 + x >= (dow if m else 0))) - d[x] + 1 for x in range(dow)]
    print(min(ans))


for _ in range(int(input())):
    main()
