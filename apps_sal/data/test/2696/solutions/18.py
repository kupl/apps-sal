n = int(input())
a = []
a = input().split(' ')
pos = n
for i in range(n - 1):
    if a[n - 1] == a[n - i - 2]:
        pos = n - i - 1
    else:
        break
print(pos)
