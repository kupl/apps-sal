h, n = map(int, input().split())

lst = [int(i) for i in input().split()]

if sum(lst) >= h:
    print("Yes")
else:
    print("No")
