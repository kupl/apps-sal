def main():
    n = int(input())
    t = list(map(int, input().split()))
    v = list(map(int, input().split()))
    back_lim = []
    lim = []
    for i in range(n):
        for _ in range(t[i]):
            back_lim.append(v[i])
            lim.append(v[i])
    back_lim.append(0)
    for i in reversed(list(range(len(back_lim)-1))):
        back_lim[i] = min(back_lim[i], back_lim[i+1]+1)
    ans = 0.0
    p = 0
    for i in range(len(back_lim)-1):
        if p < back_lim[i+1]:
            if p < lim[i]:
                ans += p + 0.5
                p += 1
            else:
                ans += p
        elif p == back_lim[i+1]:
            if p < lim[i]:
                ans += p + 0.25
            else:
                ans += p
        else:
            ans += p - 0.5
            p -= 1
    print(ans)

def __starting_point():
    main()

__starting_point()
