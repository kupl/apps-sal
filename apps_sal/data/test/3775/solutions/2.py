import sys
na, nb = list(map(int, sys.stdin.readline().split()))

al, bl = list(map(int, sys.stdin.readline().split())), list(map(int, sys.stdin.readline().split()))

a = [set((al[2*i], al[2*i+1])) for i in range(na)]
b = [set((bl[2*i], bl[2*i+1])) for i in range(nb)]

aposs, bposs = set(), set()
possible_shared = set()
i_know_a_knows, i_know_b_knows = True, True

for ahas in a:
    bposshere = set()
    for bp in b:
        if len(ahas & bp) == 1:
            bposshere |= ahas & bp
    possible_shared |= bposshere

    if len(bposshere) == 2:
        i_know_a_knows = False

for bhas in b:
    aposshere = set()
    for ap in a:
        if len(bhas & ap) == 1:
            aposshere |= bhas & ap
    possible_shared |= aposshere

    if len(aposshere) == 2:
        i_know_b_knows = False


if len(possible_shared) == 1:
    print(list(possible_shared)[0])
elif i_know_a_knows and i_know_b_knows:
    print(0)
else:
    print(-1)

