from collections import defaultdict


def main():
    n = int(input())
    s = input()
    count = len(set(s))
    d = defaultdict(int)
    res = n
    i = 0
    d[s[0]] += 1
    j = 1
    while j < n:
        if len(d) == count:
            res = min(res, j - i)
            d[s[i]] -= 1
            if d[s[i]] == 0:
                del d[s[i]]
            i += 1
        else:
            d[s[j]] += 1
            j += 1
    while len(d) == count:
        res = min(res, j - i)
        d[s[i]] -= 1
        if d[s[i]] == 0:
            del d[s[i]]
        i += 1
    print(res)


main()
