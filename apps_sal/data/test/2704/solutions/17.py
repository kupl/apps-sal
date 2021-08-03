n, q = list(map(int, input().split()))
a1 = list(map(int, input().split()))
b = min(a1)
c = max(a1)
for i in range(q):
    s = int(input())
    if(s >= b and s <= c):
        print("Yes")
    else:
        print("No")
