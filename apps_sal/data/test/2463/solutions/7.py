
n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
for i in range(0, len(a) - 1, 2):
    a[i], a[i + 1] = a[i + 1], a[i]
ans = 0
# print(a)
for i in range(0, len(a) - 1):
    if a[i] < a[i - 1] and a[i] < a[i + 1]:
        ans += 1
print(ans)
for i in range(len(a)):
    if i != len(a) - 1:
        print(a[i], end=" ")
    else:
        print(a[i])
# print()
