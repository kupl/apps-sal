a = input().split()
a = [int(i) for i in a]

if a[0] <= a[1]:
    print("unsafe")
else:
    print("safe")
