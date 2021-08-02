n = int(input())
L = list(map(int, input().split()))
if sum(L) - max(L) > max(L):
    print("Yes")
else:
    print("No")
