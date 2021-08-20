n = int(input())
names = []
for i in range(n):
    names.append(input().split())
a = list(map(int, input().split()))
for i in range(n):
    a[i] -= 1
p = [0] * n
for i in range(n):
    p[a[i]] = i
ans = 'YES'
choice = 0
for i in range(n - 1):
    if choice == 0:
        if min(names[a[i]][0], names[a[i]][1]) > max(names[a[i + 1]][0], names[a[i + 1]][1]):
            ans = 'NO'
        elif min(names[a[i]][0], names[a[i]][1]) > names[a[i + 1]][0]:
            choice = 2
        elif min(names[a[i]][0], names[a[i]][1]) > names[a[i + 1]][1]:
            choice = 1
    elif choice == 1:
        if names[a[i]][0] > max(names[a[i + 1]][0], names[a[i + 1]][1]):
            ans = 'NO'
        elif names[a[i]][0] > names[a[i + 1]][0]:
            choice = 2
        elif names[a[i]][0] > names[a[i + 1]][1]:
            choice = 1
        else:
            choice = 0
    elif choice == 2:
        if names[a[i]][1] > max(names[a[i + 1]][0], names[a[i + 1]][1]):
            ans = 'NO'
        elif names[a[i]][1] > names[a[i + 1]][0]:
            choice = 2
        elif names[a[i]][1] > names[a[i + 1]][1]:
            choice = 1
        else:
            choice = 0
print(ans)
