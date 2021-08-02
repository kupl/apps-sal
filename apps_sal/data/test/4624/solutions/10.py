def ii(): return int(input())
def li(): return list(map(int, input().split()))


t = int(input())

for _ in range(t):
    n, x = list(map(int, input().split()))

    for i in range(n):
        if i * x + 2 >= n:
            print(i + 1)
            break
