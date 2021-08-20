N = int(input())
H = list(map(int, input().split()))
H.append(10 ** 10)
lst = []
count = 0
for i in range(N):
    if H[i] < H[i + 1]:
        lst.append(i)
        count += 1
lst2 = []
for n in range(count):
    if n == 0:
        x = lst[n] - 0
        lst2.append(x)
    else:
        y = lst[n] - lst[n - 1] - 1
        lst2.append(y)
print(max(lst2))
