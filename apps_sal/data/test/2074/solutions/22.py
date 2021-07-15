n,m = map(int,input().split())
print(max([min(list(map(int,input().split()))) for _ in range(n)]))
