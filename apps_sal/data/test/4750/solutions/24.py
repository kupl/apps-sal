n = int(input())
for i in range(n):
    l1, r1, l2, r2 = list(map(int, input().split()))
    if(l1 == l2):
        l2 = r2
    print(l1, l2)
