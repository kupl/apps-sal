n = int(input())
a = list(map(int, input().split()))
fixed = extra = 0
for i in range(n):
    if a[i] == i:
        fixed += 1
    elif a[a[i]] == i:
        extra = 2
    elif not extra:
        extra = 1
print(fixed + extra)

