import sys
sys.setrecursionlimit(10 ** 7)
arr = ['a', 'b', 'c']
savelis = [0] * 10


def main():
    (N, K) = list(map(int, input().split()))
    Flis = list(map(int, input().split()))
    Tlis = [i for i in range(10)]
    Tlis = [i for i in Tlis if i not in Flis]
    str_flis = [str(i) for i in Flis]
    ANS = []
    for i in range(N * 10):
        stri = str(i)
        TF = True
        for j in stri:
            if j in str_flis:
                TF = False
                break
        if TF:
            ANS.append(i)
    for item in ANS:
        if item >= N:
            print(item)
            break


def __starting_point():
    main()


__starting_point()
