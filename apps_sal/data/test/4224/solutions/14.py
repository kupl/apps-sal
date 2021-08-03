'''
Created on 2020/08/17

@author: harurun
'''


def main():
    import sys
    pin = sys.stdin.readline
    pout = sys.stdout.write
    perr = sys.stderr.write

    N = int(pin())
    a = list(map(int, pin().split()))
    ans = 0
    for i in a:
        if i % 2 == 1:
            continue
        t = i
        while True:
            if t % 2 == 0:
                t = t // 2
                ans += 1
            else:
                break
    print(ans)
    return


main()
