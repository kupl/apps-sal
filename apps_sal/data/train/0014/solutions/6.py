q = int(input())

for _ in range(q):
    a, b = list(map(int, input().split()))
    c, d = list(map(int, input().split()))
    a, b = min(a, b), max(a, b)
    c, d = min(c, d), max(c, d)
    if b == d and a+c == b:
        print("Yes")
    else:
        print("No")


