#! /usr/bin/python
# kmwho
# Codeforces 401 D2

def main():
    n = int(input())
    x = int(input())
    n = n % 6
    pos = [ 0,1,2 ]
    for i in range(1,n+1):
        if i%2 == 1:
            pos[0],pos[1] = pos[1], pos[0]
        else:
            pos[1],pos[2] = pos[2], pos[1]
    print(pos[x])


main()


