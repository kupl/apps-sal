q = int(input())
for rwer in range(q):
    (n, m) = map(int, input().split())
    l = list(map(int, input().split()))
    print(min(m, sum(l)))
