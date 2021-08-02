from sys import stdin


def binary(A, x):
    N = len(A)
    low, hi = 0, N
    while low + 1 != hi:
        mid = low + ((hi - low) >> 1)
        if x < A[mid]: hi = mid
        else: low = mid
    return low


def main():
    s, b = stdin.readline().split()
    line = list(map(int, stdin.readline().split()))
    gold = {}
    l = list()
    for _ in range(int(b)):
        d, g = map(int, stdin.readline().split())
        if gold.get(d) == None:
            gold[d] = g
            l.append(d)
        else:
            gold[d] += g
    l.sort()
    i = 1
    while i < len(l):
        gold[l[i]] += gold[l[i - 1]]
        i += 1
    s = int(s)
    for i in range(s):
        it = binary(l, line[i])
        if(i == s - 1):
            if(it == 0 and line[i] < l[it]):
                print(0)
            else:
                print(gold[l[it]])
        else:

            if(it == 0 and line[i] < l[it]):
                print(0, end=" ")
            else:
                print(gold[l[it]], end=" ")


main()
