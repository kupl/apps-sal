from sys import stdin

def func(n):
    if n == 1:
        return 0
    x = n//2
    m = 0
    while(x > 0):
        m += 4*(n -1)*x
        x -= 1
        n -= 2
    return m

for _ in range(int(input())):
    n = int(input())
    #l = list(map(int, stdin.readline().split()))
    #n, k = map(int, input().split())
    print(func(n))

