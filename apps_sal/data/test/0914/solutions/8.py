import sys
import math
sys.setrecursionlimit(100000)

#sys.stdin = open("INP.txt", 'r')
# sys.stdout = open("OUT.txt", 'w')


def main():
    s = input()
    n = int(input())
    M = dict()
    for char in s:
        if char in M:
            M[char] += 1
        else:
            M[char] = 1
    if n < len(M):
        print(-1)
    else:
        l = 1
        r = len(s)
        while l != r:
            k = l + (r - l) // 2
            smallest_n = 0
            for it in list(M.values()):
                tmp = math.ceil(it / k)
                smallest_n += tmp
            if smallest_n <= n:
                r = k
            else:
                l = k + 1
        sticker = ''
        for char, occ in zip(list(M.keys()), list(M.values())):
            sticker += (char * math.ceil(occ / l))

        if len(sticker) < n:
            sticker += (n - len(sticker)) * list(M.keys())[0]
        print("{}\n{}".format(l, sticker))


main()
