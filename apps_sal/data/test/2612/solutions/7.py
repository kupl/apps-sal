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
    s = [0] + [int(x) for x in input().split()]
    L = [1] * len(s)
    for i in range(1, len(L)):
        ptr = i + i
        while ptr <= n:
            if s[ptr] > s[i]:
                L[ptr] = max(L[ptr], L[i] + 1)
            ptr += i
    print(max(L))
