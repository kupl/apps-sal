input()
a = list(map(int, input().split()))
b = []
for i in range(1, len(a)):
    if a[i] == 1:
        b += [a[i - 1]]
b += [a[-1]]
print(len(b))
print(*b)
