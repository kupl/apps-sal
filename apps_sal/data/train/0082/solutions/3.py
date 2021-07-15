for _ in range(int(input())):
    n=int(input())
    print(*[*map(int,input().split())][::-1])
