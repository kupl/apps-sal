q = int(input())

for _ in range(q):
    n, m = list(map(int, input().split()))
    if n == 2 and m == 2 or n == 1 or m == 1:
        print("YES")
    else:
        print("NO")

