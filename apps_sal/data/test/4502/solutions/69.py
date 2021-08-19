"""
Created on 2020/08/28

@author: harurun
"""


def main():
    from collections import deque
    import sys
    pin = sys.stdin.readline
    pout = sys.stdout.write
    perr = sys.stderr.write
    n = int(pin())
    a = list(map(int, pin().split()))
    b = deque([])
    if n % 2 == 0:
        for i in range(n):
            if i % 2 == 0:
                b.append(a[i])
            else:
                b.appendleft(a[i])
    else:
        for j in range(n):
            if j % 2 == 0:
                b.appendleft(a[j])
            else:
                b.append(a[j])
    for k in range(n):
        pout(str(b[k]))
        if k != n - 1:
            pout(' ')
    pout('\n')
    return


main()
