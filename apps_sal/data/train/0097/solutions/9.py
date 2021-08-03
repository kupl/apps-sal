from string import ascii_uppercase

a = ascii_uppercase
N = int(input())

for i in range(N):
    me, comp = input().split(' ')
    # Want to maximize the lexicographic swap
    best = ''.join(sorted(me))
    # print(best)

    mismatch = -1
    for index, pair in enumerate(zip(best, me)):
        i, j = pair
        if i != j:
            mismatch = index
            break

    if mismatch != -1:
        # Want to swap mismatch (index) with last occurence after mismatch
        swaploc = len(me) - me[mismatch + 1:][::-1].find(best[mismatch]) - 1
        swap1 = me[:mismatch] + me[swaploc] + me[mismatch + 1:swaploc] + me[mismatch] + me[swaploc + 1:]
    else:
        swap1 = me
    if swap1 < comp:
        print(swap1)
    else:
        print('---')
