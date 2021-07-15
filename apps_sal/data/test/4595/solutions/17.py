#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    S = input()
    search_string=['A','Z']
    position=[]

#Aを探す
    for i,s in enumerate(S):
        if s==search_string[0]:
            position.append(i)
            break

#Zを探す
    for r_i,r_s in enumerate(reversed(S)):
        if r_s==search_string[1]:
            position.append(len(S)-r_i)
            break

    print(position[1]-position[0])

def __starting_point():
    main()
__starting_point()
