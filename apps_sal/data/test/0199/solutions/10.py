import math, sys, itertools

def mp():
    return list(map(int, input().split()))

def main():
    n, s = mp()
    a = mp()
    sm = sum(a)
    if sm < s:
        print(-1)
        return
    ans = (sum(a) - s) // n
    print(min(ans, min(a)))
        

deb = 0
if deb:
    file = open('input.txt', 'r')
    input = file.readline
else:
    input = sys.stdin.readline
    
main()
