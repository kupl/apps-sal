import sys

input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = 10**5
    l = [0]*m
    for i in range(n):
        if a[i] >= 1:
            l[a[i]-1] += 1
        l[a[i]] += 1
        if a[i] < m-1:
            l[a[i]+1] += 1
    print(max(l))

def __starting_point():
    main()
__starting_point()
