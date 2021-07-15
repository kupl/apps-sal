import sys

def main():
    m,d = map(int,sys.stdin.readline().split())
    x = [31,28,31,30,31,30,31,31,30,31,30,31]
    y = x[m-1] + d-1
    res = y/7
    if res > int(res):
        res = int(res)+1
    print(int(res))

main()
