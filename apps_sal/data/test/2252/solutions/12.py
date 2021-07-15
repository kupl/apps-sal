def main():
    R = lambda: map(int, input().split())
    n, m = R()
    p = [0] + list(R())
    for _ in range(m):
        l, r, x = R()
        v = p[x]
        c = sum(map(lambda x: x < v, p[l:r+1]))
        print('Yes' if c == x - l else 'No')
main()
