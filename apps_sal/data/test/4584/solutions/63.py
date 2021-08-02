n = int(input())
a = list(map(int, input().split()))

ans = [0] * n

for x in a:
    ans[x - 1] += 1


for x in ans:
    print(x)
