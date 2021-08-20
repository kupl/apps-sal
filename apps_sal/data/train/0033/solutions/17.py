"""T=int(input())
for _ in range(0,T):
    n=int(input())
    a,b=map(int,input().split())
    s=input()
    s=[int(x) for x in input().split()]
    for i in range(0,len(s)):
        a,b=map(int,input().split())"""
T = int(input())
for _ in range(0, T):
    n = int(input())
    print(2)
    num = n
    for i in range(n - 1, 0, -1):
        print(i, num)
        if (num + i) % 2 == 0:
            num = (num + i) // 2
