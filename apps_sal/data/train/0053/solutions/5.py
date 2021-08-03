def solve1(n, comps):
    ans = []
    rng = iter(list(range(1, n + 1)))
    for comp in [len(comp) + 1 for comp in comps.split(">")][::-1]:
        ans.append([ansi for (_, ansi) in zip(list(range(comp)), rng)])
    fin_ans = []
    ans.reverse()
    for ansi in ans:
        fin_ans.extend(ansi)
    return fin_ans


def solve2(n, comps):
    ans = []
    rng = iter(list(range(1, n + 1)))
    for comp in [len(comp) + 1 for comp in comps.split("<")]:
        ans.extend([ansi for (_, ansi) in zip(list(range(comp)), rng)][::-1])
    return ans


def main():
    for _ in range(int(input())):
        n, comps = input().split()
        n = int(n)
        print(*solve1(n, comps))
        print(*solve2(n, comps))


main()
