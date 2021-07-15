import bisect
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cnt = [0] * n
    for val in b:
        cnt[val] += 1

    all_set = sorted(set(b))
    #print(all_set)
    n_all_set = len(all_set)

    nextL = [0] * n
    nextR = [0] * n
    for i in range(1, n_all_set):
        nextL[all_set[i]] = all_set[i-1]
        #print('l',nextL)
    for i in range(n_all_set-1):
        nextR[all_set[i]] = all_set[i+1]
        #print('r',nextR)

    nextR[all_set[-1]] = all_set[0]
    nextL[all_set[0]] = all_set[-1]
    #print(nextR,nextL)

    res = []

    def opositeMod(x):
        return 0 if x == 0 else n-x

    for val in a:
        cand_pos = bisect.bisect_left(all_set, opositeMod(val))
        if cand_pos == n_all_set:
            cand_pos = 0

        cand_val = all_set[cand_pos]

        if cnt[cand_val] == 0:
            to_update = []
            current = nextR[cand_val]
            while cnt[current] == 0:
                to_update.append(current)
                current = nextR[current]
            for upd in to_update:
                nextR[upd] = current
                nextL[upd] = nextL[current]
            cand_val = current

        res.append((val+cand_val) % n)
        cnt[cand_val] -= 1
        if cnt[cand_val] == 0:
            nextL[nextR[cand_val]] = nextL[cand_val]
            nextR[nextL[cand_val]] = nextR[cand_val]
            #print(nextR,nextL)

    print(*res)

def __starting_point():
    main()

__starting_point()
