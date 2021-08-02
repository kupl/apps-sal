a = list(map(int, input()));
cnts = [0] * 10;
for aa in a:
    cnts[aa] += 1

mem = {}

mem[(1, 0, 0, 0, 0, 0, 0, 0, 0, 0)] = 0;

for i in range(1, 10):
    mem[(0,) * (i) + (1,) + (0,) * (10 - i - 1)] = 1;


def get(a):
    if (tuple(a) in mem):
        return mem[tuple(a)]
    else:
        aa = list(a)
        tot = 0
        for i in range(0, 10):
            if (a[i] != 0):
                aa[i] -= 1;
                tot += get(aa);
                aa[i] += 1;
        mem[tuple(a)] = tot
        return tot


bigTot = 0


def goThrough(pre, post):
    nonlocal bigTot
    if (len(post) == 0):
        bigTot += get(pre)
    elif (post[0] == 0):
        goThrough(pre + (0,), post[1:])
    else:
        for i in range(1, post[0] + 1):
            goThrough(pre + (i,), post[1:])


goThrough((), cnts)

print(bigTot)
