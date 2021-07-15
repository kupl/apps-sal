n, k, q = map(int, input().split())
b = [k - q] * n

for i in range(q):
    ai = int(input())
    b[ai - 1] += 1

for j in range(n):
    if b[j] > 0:
        print("Yes")
    else:
        print("No")
