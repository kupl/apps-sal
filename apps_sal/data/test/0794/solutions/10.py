def main():
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    if sum(a[:n]) == sum(a[n:]):
        print(-1)
    else:
        print(*a)



main()

