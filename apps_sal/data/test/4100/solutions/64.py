n, k, q = map(int, input().split())
point = [k] * (n)
for _ in range(q):
    a = int(input())
    point[a - 1] += 1
for i in range(n):
    if point[i] - q > 0:
        print("Yes")
    else:
        print("No")
