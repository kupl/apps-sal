#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    O = input().rstrip()
    E = input().rstrip()
    password=""
    last = ""

    if len(O) > len(E):
        last = O[-1]
    elif len(O) < len(E):
        last = E[-1]
    else:
        last=""

    for p1,p2 in zip(O,E):
        password+=p1+p2
    print(password+last)

def __starting_point():
    main()
__starting_point()
