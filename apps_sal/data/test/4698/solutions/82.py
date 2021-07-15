n = int(input())
t = list(map(int, input().split()))
m = int(input())
drink = [list(map(int, input().split())) for _ in range(m)]
for p, x in drink:
    print((sum(t) - t[p - 1] + x))

