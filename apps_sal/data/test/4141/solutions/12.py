n = int(input())
a = list(map(int, input().split()))
check = True
for i in range(n):
    if a[i] % 2 == 0:
        if a[i] % 3 != 0 and a[i] % 5 != 0:
            check = False
print("APPROVED" if check else "DENIED")
