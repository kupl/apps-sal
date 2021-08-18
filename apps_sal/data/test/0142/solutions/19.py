from itertools import permutations

MOD = 10**9 + 7


def find_best(c):
    n = 2 ** len(c)
    best_c = c[0] * n
    best_i = 0
    for i, ci in enumerate(c):
        if n // (2**i) * c[i] < best_c:
            best_c = n // (2**i) * c[i]
            best_i = i
    return best_i


def main():
    n, l = [int(c) for c in input().split(' ')]
    c = [int(c) for c in input().split(' ')]
    ans = []
    cur_ans = 0
    while l:
        ind = find_best(c[:n])
        vol = 2**ind
        cnt = l // vol
        l %= vol
        cur_ans += cnt * c[ind]
        ans.append(cur_ans + (l % vol and c[ind] or 0))
        n = ind
    print(min(ans))


while 1:
    main()
    break
