n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
l = min(a)
h = max(a)
for i in range(k):
    q = int(input())
    if q >= l and q <= h:
        print("Yes")
    else:
        print("No")
