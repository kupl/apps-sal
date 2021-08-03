n = int(input())
a = list(map(int, input().split()))
i = 0
j = n - 1
b = [0] * 2
t = 0
while i <= j:
    if a[i] > a[j]:
        b[t] += a[i]
        i += 1
    else:
        b[t] += a[j]
        j -= 1
    t ^= 1
print(b[0], b[1])
