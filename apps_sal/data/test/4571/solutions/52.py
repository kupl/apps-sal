# coding = SJIS

n, m = map(int, input().split())

print((100 * (n - m) + 1900 * m) * (2 ** m))
