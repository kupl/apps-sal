t = int(input())
for _ in range(t):
    n = int(input()); a = sorted(list(map(int, input().split())))
    print("First") if n%2 == 0 and a[::2] != a[1::2] else print("Second")
