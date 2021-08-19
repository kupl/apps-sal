n = int(input())
m = list(map(int, input().split()))
for i in range(n):
    if m[i] % 2 == 0:
        m[i] -= 1
    print(m[i], end=' ')
