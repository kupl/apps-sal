from sys import stdin, stdout


def find(arr, N):
    S = set([0])
    r = 0
    k = 0
    for i in arr:
        r += i
        if r in S:
            k += 1
            S = set([0])
            r = i
        S.add(r)
    return k


def main():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    print(find(arr, N))


main()
