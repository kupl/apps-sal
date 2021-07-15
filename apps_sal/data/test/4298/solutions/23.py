N,D = [int(v) for v in input().split()]
ans = int(N / (2*D + 1)) + int(N % (2*D+1) != 0)
print(ans)

