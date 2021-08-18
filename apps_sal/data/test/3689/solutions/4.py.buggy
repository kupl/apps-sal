import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
a = list(input())

for i in range(n):
    a[i] = int(a[i])

for i in range(n):
    if a[i] < a[i % k]:
        b = [0] * n
        for i in range(n):
            b[i] = a[i % k]
        print(n)
        print("".join(map(str, b)))
        return
    if a[i] > a[i % k]:
        break
else:
    b = [0] * n
    for i in range(n):
        b[i] = a[i % k]
    print(n)
    print("".join(map(str, b)))
    return

for i in range(k)[::-1]:
    if i == k - 1 and a[i] != 9:
        a[i] += 1
        break
    if a[i] == 9:
        a[i] = 0
    else:
        a[i] += 1
        break
for i in range(n):
    a[i] = a[i % k]
print(n)
print("".join(map(str, a)))
