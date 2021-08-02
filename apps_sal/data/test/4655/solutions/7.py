n = int(input())
for _ in range(n):
    l = list(map(int, input().split()))
    s = sum(l)
    print(s // 2)
