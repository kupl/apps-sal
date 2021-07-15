def main():
    n, *target = list(map(int, input().split()))
    l = [int(input()) for _ in range(n)]
    ans = float("inf")
    base = 4
    for i in range(pow(base, n)):
        now_l = [0] * base
        add = [0] * base
        now = i
        for j in range(n):
            now_l[now % base] += l[j]
            add[now % base] += 1
            now //= base
        if 0 in now_l[:base - 1]:
            continue
        now_ans = sum([abs(target[i] - now_l[i]) for i in range(3)]) + (sum(add[:3]) - 3) * 10
        ans = min(ans, now_ans)
    print((0 if all(t in l for t in target) else ans))


def __starting_point():
    main()

__starting_point()
