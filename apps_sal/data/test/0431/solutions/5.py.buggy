n, m = list(map(int, input().split()))
L = [list(input()) for i in range(n)]
light_floors = [n - i - 1 for i in range(n) if "1" in L[i]]
if len(light_floors) == 0:
    print(0)
    return
limit = max(light_floors)


def rec(i, lst):
    if i == limit:
        # first: left
        # print(list(reversed(L[-1])))
        if "1" in L[-1]:
            cnt = m + 2 - list(reversed(L[-1])).index("1") - 1
        else:
            cnt = 0
        now = cnt
        for j, l in enumerate(lst):
            if l == "l":
                cnt += now
                cnt += 1
                if "1" in L[-1 - j - 1]:
                    next_pos = (m + 2 - list(reversed(L[-1 - j - 1])).index("1") - 1)
                else:
                    next_pos = 0
                cnt += next_pos
                now = next_pos
            else:
                cnt += (m + 2 - now - 1)
                cnt += 1
                if "1" in L[-1 - j - 1]:
                    next_pos = L[-1 - j - 1].index("1")
                else:
                    next_pos = m + 2 - 1
                cnt += (m + 2 - next_pos - 1)
                now = next_pos
        return cnt

    return min(rec(i + 1, lst + ["l"]), rec(i + 1, lst + ["r"]))


print(rec(0, []))
