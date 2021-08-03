n, m = map(int, input().split())
l = [0 for i in range(120)]
l[0] = 1
for i in range(n):
    a, b = map(int, input().split())
    for i in range(a + 1, b + 1):
        l[i] = 1
for i in range(0, m + 1):
    if l[i] == 0:
        print("NO")
        return
print("YES")
