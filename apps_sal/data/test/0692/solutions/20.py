n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
ans = 0
for i in range(1000000):
    for j in range(n):
        if i % a[j] == b[j]:
            ans += 1
            break
print(ans / 1000000)
