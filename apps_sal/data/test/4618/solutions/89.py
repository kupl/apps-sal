from collections import deque
s = input()
k = int(input())


def index_Multi(List, liter):
    index_L = []
    for val in range(0, len(List)):
        if liter == List[val]:
            index_L.append(val)
    return index_L


def substr(s, k, j):
    n = ord('a')
    while True:
        l = index_Multi(s, chr(n + j))
        word = []
        if len(l) == 0:
            n += 1
        else:
            for p in l:
                for i in range(k):
                    word.append(s[p:p + i + 1])
            sword = set(word)
            if len(sword) >= k:
                tword = list(sword)
                tword.sort()
                return tword[k - 1]
            else:
                return substr(s, k - len(sword), j + 1)
            break


print(substr(s, k, 0))
