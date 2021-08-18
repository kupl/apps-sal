n = int(input())
a = list(map(int, input().split()))
for i in range(n - 1):
    s = sorted((a[i], a[i + 1]))
    for j in range(i):
        lst = sorted((a[j], a[j + 1]))
        if lst[0] < s[0] < lst[1] < s[1] or s[0] < lst[0] < s[1] < lst[1]:
            print("yes")
            return
print("no")
