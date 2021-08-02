a = list(map(int, input().split()))
for i in range(4):
    if a[i] == sum(a) - a[i]:
        print("Yes")
        return
for i in range(1, 4):
    if a[0] + a[i] == sum(a) - (a[0] + a[i]):

        print("Yes")
        return
print("No")
