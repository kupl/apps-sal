n, m = list(map(int, input().split()))
like = [0] * m

for i in range(n):
    a = list(map(int, input().split()))[1:]
    for j in a:
        like[j - 1] += 1

print((sum(i == n for i in like)))
