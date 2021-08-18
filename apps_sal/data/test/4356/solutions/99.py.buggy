n, m = map(int, input().split())
a = []
b = []
for _ in range(n):
    a.append(input())
for _ in range(m):
    b.append(input())
for i in range(n - m + 1):
    if b[i] in a[i]:
        for x in range(m - 1):
            if b[i + x] not in a[i + x]:
                print("No")
                return
        print("Yes")
        return
    else:
        print("No")
        return
