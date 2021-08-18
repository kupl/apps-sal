a, b = map(int, input().split())

ans = [["

for i in range(a - 1):
    rows = (i // 50) * 2
    clms = (i % 50) * 2
    ans[rows * 2][clms] = "."

for i in range(b - 1):
    rows = (i // 50) * 2
    clms = (i % 50) * 2
    ans[99 - rows][clms] = "

print(100, 100)
for a in ans:
    print("".join(a))
