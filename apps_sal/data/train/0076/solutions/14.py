import sys


def second(ele):
    return(ele[1])


for _ in range(int(input())):
    n = int(input())
    if(n % 4 == 0):
        print("YES")
    else:
        print("NO")
