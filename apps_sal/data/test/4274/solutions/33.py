from sys import setrecursionlimit, exit
setrecursionlimit(1000000000)

def main():
    n, m = map(int, input().split())
    if n == m:
        print('Yes')
    else:
        print('No')

main()
