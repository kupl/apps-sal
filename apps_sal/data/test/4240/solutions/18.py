#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main(): 
    s = list(input().rstrip())
    t = input().rstrip()
    for i in range(len(s)):
        if t == "".join(s):
            print("Yes")
            return
        else:
            tmp=s.pop(0)
            s.append(tmp)
    print("No")



def __starting_point():
    main()
__starting_point()
