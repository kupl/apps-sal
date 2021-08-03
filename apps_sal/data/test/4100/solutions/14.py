n, k, q = map(int, input().split())
p = [k - q] * n
first = 0
for i in range(q):
    a = int(input())
    p[a - 1] += 1
for i in p:
    if i <= 0:
        print("No")
    else:
        print("Yes")
