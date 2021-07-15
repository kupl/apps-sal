n, d = map(int, input().split())
a = sorted(list(map(int, input().split())))
m = int(input())
print(sum(a[:m])) if m <= n else print(sum(a) - (m-n) * d)

