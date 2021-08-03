n = int(input())
a = [int(o) for o in input().split()]
ok = True
for i in range(n):
    if a[i] % 2:
        continue
    if a[i] % 3 != 0 and a[i] % 5 != 0:
        ok = False
print("APPROVED" if ok else "DENIED")
