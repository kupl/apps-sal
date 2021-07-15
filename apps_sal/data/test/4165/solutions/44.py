N = int(input())
L = list(map(int,input().split()))

theory = (max(L) < (sum(L) - max(L)))

if theory:
    print("Yes")
else:
    print("No")
