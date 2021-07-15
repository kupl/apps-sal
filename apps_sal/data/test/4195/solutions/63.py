D,N = map(int,input().split())

ans = (100 ** D) * (N if N < 100 else 101)

print(ans)
