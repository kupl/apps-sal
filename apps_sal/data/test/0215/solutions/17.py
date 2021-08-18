def solve():

    n = int(input())
    sentence = input()

    alpha = "abcdefghijklmnopqrstuvwxyz"
    alp = [[]]

    for st in sentence:
        if st in alpha:
            if st not in alp[-1]:
                alp[-1].append(st)
        else:
            alp.append([])

    return max([len(e) for e in alp])


print(solve())
