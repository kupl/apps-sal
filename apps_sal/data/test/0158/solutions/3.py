n = int(input())
a = list(map(int, input().split()))

f = True

a.sort()

if a[n] == a[n - 1]:
    f = False

if f == True:
    print("YES")
else:
    print("NO")
