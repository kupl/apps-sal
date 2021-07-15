import sys
import cProfile
input = sys.stdin.readline
def main():
    n=int(input())
    a=[int(input()) for _ in range(n)]
    l=[1]
    i=0
    aa=1
    while True:
        aa=a[aa-1]
        if aa == 2:
            print(i+1)
            return
        if i>n:
            print(-1)
            return
        i+=1
main()
