t = int(input())
for _ in range(t):
    n = int(input())
    s = [int(x) for x in input().split()]
    s = sorted(s)
    print (abs(s[n]-s[n-1]))
