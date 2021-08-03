n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]
ame = []
for i in range(n):
    ame.append(sum(a[0][:i + 1]) + sum(a[1][i:]))
print(max(ame))
