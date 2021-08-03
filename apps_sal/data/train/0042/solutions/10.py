import sys
import math
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()


for t in range(int(input())):
    ans = 0
    s = input()

    i = 0
    while i < len(s):
        if s[i] == "1":
            ans += 1
            j = i - 1
            zero_cnt = 0
            while j >= 0 and s[j] == "0":
                zero_cnt += 1
                j -= 1

            k = i
            b = "1"
            while k + 1 < len(s) and (int(b + s[k + 1], 2) - len(b) - 1 <= zero_cnt):
                ans += 1
                b += s[k + 1]
                k += 1

        i += 1

    print(ans)
