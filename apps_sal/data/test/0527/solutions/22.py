from string import ascii_lowercase
from bisect import bisect_right, bisect_left


def main():
    s = input()
    t = input()
    len_s = len(s)
    s_all = {s: [] for s in ascii_lowercase}
    for i in range(len_s):
        s_all[s[i]].append(i + 1)
    ans = 0
    if any(s_all[tt] == [] for tt in t):
        ans = -1
    else:
        s_ind = 1
        for ss in ascii_lowercase:
            s_all[ss].sort()
        for i in range(len(t)):
            next_ind = bisect_left(s_all[t[i]], s_ind)
            if next_ind == len(s_all[t[i]]):
                ans += len_s - s_ind + 1
                ans += s_all[t[i]][0]
                s_ind = s_all[t[i]][0] + 1
            else:
                ans += s_all[t[i]][next_ind] - s_ind + 1
                s_ind = s_all[t[i]][next_ind] + 1
    print(ans)


def __starting_point():
    main()

__starting_point()
