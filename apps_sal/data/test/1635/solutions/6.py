n = int(input())
a = list(map(int, input().split()))
l = [-1 for i in range(2 * 10 ** 5 + 10)]
for i in range(n):
    l[a[i]] = i
min_pos = 3 * 10 ** 5
min_s = -1
for i in range(2 * 10 ** 5 + 5):
    if l[i] == -1:
        pass
    elif l[i] < min_pos:
        min_pos = l[i]
        min_s = i
print(min_s)
