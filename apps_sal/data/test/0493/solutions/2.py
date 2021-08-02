def num_standing(s):
    ret = 0
    l = [i for i, x in enumerate(s) if x == "L"]
    r = [i for i, x in enumerate(s) if x == "R"]
    for i in range(len(l)):
        if l[i] % 2 == r[i] % 2:
            ret += 1
    for i in range(1, len(r)):
        ret += r[i] - l[i - 1] - 1
    return ret


n = int(input())
s = input()

L_i = [i for i, x in enumerate(s) if x == "L"]
R_i = [i for i, x in enumerate(s) if x == "R"]

if len(L_i) == 0 and len(R_i) == 0:
    print(n)
elif len(L_i) == 0:
    print(R_i[0])
elif len(R_i) == 0:
    print(n - L_i[0] - 1)
else:
    standing = 0
    # there are both L and R
    if R_i[0] < L_i[0]:
        # R comes first
        standing += R_i[0]
        if R_i[-1] > L_i[-1]:
            standing += R_i[-1] - L_i[-1] - 1
        else:
            standing += n - L_i[-1] - 1
        standing += num_standing(s[R_i[0]:L_i[-1] + 1])

    else:
        # L comes first
        standing += R_i[0] - L_i[0] - 1
        if R_i[-1] > L_i[-1]:
            standing += R_i[-1] - L_i[-1] - 1
        else:
            standing += n - L_i[-1] - 1
        standing += num_standing(s[R_i[0]:L_i[-1] + 1])
        if len(L_i) == 1 and len(R_i) == 1:
            standing //= 2
    print(standing)
