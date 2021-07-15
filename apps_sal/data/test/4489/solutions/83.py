#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    n = int(input())
    word_dict={}
    for i in range(n):
        s = input().rstrip()
        if s not in word_dict:
            word_dict[s]=1
        else:
            word_dict[s]+=1
    m = int(input())
    for j in range(m):
        t= input().rstrip()
        if t in word_dict:
            word_dict[t]-=1
        else:
            word_dict[t]=-1

    if max(word_dict.values()) < 0:
        print(0)
    else:
        print(max(word_dict.values()))

def __starting_point():
    main()
__starting_point()
