a = 30030
n = int(input())
m = [int(_) for _ in input().split()]
r = [int(_) for _ in input().split()]
ans = 0
for i in range(a):
    for j in range(n):
        if i % m[j] == r[j]:
            ans += 1
            break
print(ans / a)

