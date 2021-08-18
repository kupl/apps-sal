from collections import Counter


def main():
    S = input()
    A = list(map(int, S))[::-1]
    mod = []
    ten = 10
    for i in range(len(A)):
        if i == 0:
            mod += A[i],
        else:
            mod += (mod[i - 1] + ten * A[i]) % 2019,
            ten = (ten * 10) % 2019
    mod += 0,

    C = Counter(mod)
    print(sum([c * (c - 1) // 2 for c in C.values()]))


main()
