from sys import setrecursionlimit, exit
setrecursionlimit(1000000000)

def main():
    a, b = map(int, input().split())
    if a <= b:
        print(str(a) * b)
    else:
        print(str(b) * a)

main()
