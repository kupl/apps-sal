"""
Created on 2020/10/01

@author: harurun
"""
import sys
pin = sys.stdin.readline


def main():
    N = int(pin())
    a = list(map(int, pin().split()))
    d = [0] * 9
    for i in a:
        if i >= 3200:
            d[-1] += 1
            continue
        d[i // 400] += 1
    ans = 0
    for i in d[:-1]:
        if i != 0:
            ans += 1
    if ans == 0:
        print(f'{1} {d[-1]}')
        return
    print(f'{ans} {ans + d[-1]}')
    return


main()
