n = int(input())
bl = list(map(int, input().split()))
al = [0] * n
al[0] = bl[0]
al[-1] = bl[-1]

for i in range(n - 2):
    al[i + 1] = min(bl[i], bl[i + 1])

print(sum(al))
