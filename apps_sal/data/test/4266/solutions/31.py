k, x = map(int, input().split())
N=1000000
print(*list(range(max(x-k, -N)+1, min(x+k, N))))
