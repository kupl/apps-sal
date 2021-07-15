import sys
from collections import defaultdict
import bisect
def input(): return sys.stdin.readline().rstrip()


def main():
    s = list(input())
    t = list(input())
    dic = defaultdict(list)
    for index, string in enumerate(s):
        dic[string].append(index)
    cycle = 0
    ind = -1
    for string in t:
        if dic[string] == []:
            print(-1)
            return
        elif dic[string][-1] <= ind:
            cycle += 1
            ind = dic[string][0]
        else:  # [2,6,7,10] 6の次は？
            ind = dic[string][bisect.bisect_right(
                dic[string], ind)]  # n以下の個数を数える
    print(cycle*len(s)+ind+1)


def __starting_point():
    main()
__starting_point()
