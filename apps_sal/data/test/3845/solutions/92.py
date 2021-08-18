a, b = map(int, input().split())
print(100, 100)
ans = [list("
for i in range(a - 1):
    h=(i // 50) * 2
    w=(i % 50) * 2
    ans[h][w]="."
for i in range(b - 1):
    h=(i // 50) * 2 + 51
    w=(i % 50) * 2
    ans[h][w]= "
for i in ans:
    print("".join(i))
