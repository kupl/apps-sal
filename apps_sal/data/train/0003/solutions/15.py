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
    (n, k) = list(map(int, input().split()))
    s = [int(x) for x in input().split()]
    s.sort()
    s = s[::-1]
    for i in range(1, min(k + 1, len(s))):
        s[0] += s[i]
    print(s[0])
