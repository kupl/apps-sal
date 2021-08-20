n = int(input())
an = list(map(int, input().split()))
bn = list(map(int, input().split()))
cn = list(map(int, input().split()))
sat = sum(bn)
for x in range(n - 1):
    if an[x + 1] == an[x] + 1:
        sat += cn[an[x] - 1]
print(sat)
