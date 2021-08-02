l, r = map(int, input().split())
print("YES")
for i in range(l, l - 1 + int((r - l + 1)), 2):
    print(i, end=' ')
    print(i + 1)
    i = i + 2
