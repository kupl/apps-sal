#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    gates=[]
    n,m = map(int,input().split())
    gates=[list(map(int,input().split())) for _ in range(m)]
    min_data=0
    max_data=10**5+1

    for gate in gates:
        if min_data < gate[0]:
            min_data=min(gate)
        if max_data > gate[1]:
            max_data=max(gate)
    print(len(list(range(min_data,max_data+1))))

def __starting_point():
    main()
__starting_point()
