n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]
print(max(sum(a[0][:i + 1] + a[1][i:]) for i in range(n)))
