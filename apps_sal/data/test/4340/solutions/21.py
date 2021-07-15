input()
a = list(map(int, input().split()))
for i in range(len(a)):
    if a[i] % 2 == 0:
        a[i] -= 1
print(*a)

