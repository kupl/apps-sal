#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    maps=[]
    n = int(input())
    maps=[list(map(int,input().split())) for _ in range(2)]
    dp=[]
    for i in range(n):
        total=sum(maps[0][:i+1])+sum(maps[1][i:])
        dp.append(total)
    print(max(dp))

def __starting_point():
    main()
__starting_point()
