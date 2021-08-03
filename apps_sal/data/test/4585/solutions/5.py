'''
Created on 2020/08/28

@author: harurun
'''


def main():
    import sys
    pin = sys.stdin.readline
    pout = sys.stdout.write
    perr = sys.stderr.write

    X = int(pin())
    i = 1
    while i <= X:
        if i * (i + 1) >= 2 * X:
            print(i)
            return
        i += 1
    return


main()
