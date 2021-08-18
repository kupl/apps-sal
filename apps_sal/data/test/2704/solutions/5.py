n, q = map(int, input().split())
l = [int(x) for x in input().split()]
mn = min(l)
mx = max(l)
for i in range(q):
    k = int(input())
    if(k <= mx and k >= mn):
        print("Yes")
    else:
        print("No")
