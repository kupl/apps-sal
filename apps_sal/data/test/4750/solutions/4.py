n = int(input())

for i in range(n):
    l1, r1, l2, r2 = list(map(int, input().split()))
    print(l1, r2 if r2 != l1 else l2)

