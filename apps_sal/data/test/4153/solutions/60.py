#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    S = input().rstrip()
    stack=[]
    count=0

    if S=="0":
        print("0")
        return

    for s in S:
        if len(stack)==0:
            stack.append(str(s))
        else:
            if s != stack[-1]:
                count+=1
                stack.pop()
            else:
                stack.append(str(s))
    print(2*count)

def __starting_point():
    main()
__starting_point()
