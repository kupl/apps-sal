def main():
    input()
    aa = list(map(int, input().split()))
    n = max(aa) + 1
    cnt = [0] * n
    for x in aa:
        cnt[x] += 1
    a, b = 0, cnt[1]
    for i in range(2, n):
        a, b = b, max(b, a + cnt[i] * i)
    print(b)

def __starting_point():
    main()
__starting_point()
