import math
import sys
def listinput(): return list(map(int,input().split(' ')))

def main():
    answer = ""
    for test in range(int(input())):
        n,d = listinput()
        x = 0
        broken = False
        while x*x <= d:
            if x+(d+x)//(x+1) <= n:
                answer += "YES \n"
                broken = True
                break
            x+=1
        if not broken:
            answer += "NO \n"
    print(answer)

main()
    

