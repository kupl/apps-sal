t = int(input())
for _ in range(t):
    (n, m) = list(map(int, input().split()))
    s = list(map(int, input().split()))
    print(min(m, sum(s)))
