from sys import stdin as cin
from sys import stdout as cout

def main():
    n, k = list(map(int, cin.readline().split()))
    a = list(map(int, cin.readline().split()))
    o = 864236415217
    for i in a:
        if k % i == 0:
            o = min(o, k // i)
    print(o)

main()

