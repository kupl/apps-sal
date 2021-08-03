n = int(input())
p = list(map(int, input().split()))

ans = 0
size = 998244353

for p in p:
    ans = (ans + 1) % size
    ans = (((ans * 100) % size) * pow(p, size - 2, size)) % size

print(ans)
