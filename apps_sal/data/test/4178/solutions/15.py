#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    numbers=[]
    n = int(input())
    numbers=list(map(int,input().split()))
    prev=0


    for i in numbers:
        if i==0:
            prev=i
        else:
            if prev<=i:
                prev=i
            elif prev <=i+1:
                prev=i+1
            else:
                print("No")
                return
    print("Yes")

def __starting_point():
    main()
__starting_point()
