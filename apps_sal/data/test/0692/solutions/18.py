n = int(input())
m = list(map(int, input().split()))
r = list(map(int, input().split()))

k = 0
for i in range(100000):
    for j in range(n):
        if i % m[j] == r[j]:
            k += 1
            break

print(k / 100000)
