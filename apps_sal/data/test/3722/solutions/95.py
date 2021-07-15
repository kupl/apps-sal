from itertools import product
P = 10 ** 9 + 7
F = [0, 1]
for i in range(1010):
    F.append(sum(F[-2:]) % P)
# print("F =", F[:20])
N = int(input())
AA = input()
AB = input()
BA = input()
BB = input()
P = 10 ** 9 + 7
def calc(aa, ab, ba, bb):
    if N <= 3: return 1
    ss = aa + ab + ba + bb
    if aa == "A" and bb == "B":
        return 1
    if aa == "A" and ab == "A":
        return 1
    if bb == "B" and ab == "B":
        return 1
    if ss == "ABAA" or ss == "BABB" or ss == "BABA" or ss == "BBAA":
        return pow(2, N - 3, P)
    if ss == "ABBA" or ss == "BAAB" or ss == "BAAA" or ss == "BBBA":
        return F[N-1]
    return -1
# for s in product("AB", repeat = 4):
#     print(s, calc(*s))

print(calc(AA, AB, BA, BB))
