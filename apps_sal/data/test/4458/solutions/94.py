#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    numbers=[]
    n = int(input())
    numbers=list(map(int,input().split()))
    small=0
    dp=[]

    for idx,data in enumerate(numbers):
        if idx == 0:
            small=data
            dp.append(data)
        elif data < small:
            small=data
            dp.append(data)
        else:
            continue
    print(len(dp))

def __starting_point():
    main()
__starting_point()
