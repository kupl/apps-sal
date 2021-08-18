n, q = list(map(int, input().split()))
l = list(map(int, input().split()))
mi = min(l)
mx = max(l)
for i in range(q):
    m = int(input())
    if m <= mx and m >= mi:
        print("Yes")
    else:
        print("No")
