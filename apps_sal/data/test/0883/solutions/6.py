n = int(input())
A = list(map(int, input().split()))
Cnt = sum(A)
y = 1 == (Cnt + 1) % (n + 1)
y += 1 == (Cnt + 2) % (n + 1)
y += 1 == (Cnt + 3) % (n + 1)
y += 1 == (Cnt + 4) % (n + 1)
y += 1 == (Cnt + 5) % (n + 1)
print(5 - y)
