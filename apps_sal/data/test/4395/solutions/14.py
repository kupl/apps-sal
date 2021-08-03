def diffs(s1, s2):
    c = 0
    for i, j in zip(s1, s2):
        if not i == j:
            c += 1
    return c


n = int(input())
i_s = input()
chk = int(n / 3) + 1
sl = ["RGB", "RBG", "BRG", "BGR", "GBR", "GRB"]
ol = list(map(lambda x: (x * chk)[:n], sl))
dl = list(map(lambda x: diffs(x, i_s), ol))
print(min(dl))
print(ol[dl.index(min(dl))])
