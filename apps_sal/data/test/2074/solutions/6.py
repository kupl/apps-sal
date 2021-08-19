(n, m) = map(int, input().split())
mas = []
for i in range(n):
    cur = list(map(int, input().split()))
    mas.append(min(cur))
print(max(mas))
