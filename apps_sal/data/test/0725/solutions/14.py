import sys


def main():
    
    n, m = map(int, sys.stdin.readline().split())
    
    black = True
    for i in range(n):
        s = sys.stdin.readline()
        if 'C' in s or 'M' in s or 'Y' in s:
            black = False   
      
    if black:
        print("#Black&White")
    else :
        print("#Color")

main()
