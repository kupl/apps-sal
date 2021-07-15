n = int(input())
a = []
for _ in range(2):
    a.append(list(map(int, input().split())))

b = list(map(int, input().split()))

ans = []
for i, e in enumerate(b):
    ans.append(e + sum(a[0][:i]) + sum(a[1][i:]))

print(sum(sorted(ans)[0:2]))

