def main():
    (N, M) = list(map(int, input().split()))
    digits = [-1] * N
    for _ in range(M):
        (s, c) = list(map(int, input().split()))
        s -= 1
        if ~digits[s] and digits[s] != c:
            print(-1)
            return
        digits[s] = c
    if N == 1:
        print(max(0, digits[0]))
        return
    if digits[0] == 0:
        print(-1)
        return
    if digits[0] == -1:
        digits[0] = 1
    ans = ''.join(map(str, (d if ~d else 0 for d in digits)))
    print(ans)


def __starting_point():
    main()


__starting_point()
