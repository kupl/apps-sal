n,k = map(int,input().split())
a = sorted(map(int,input().split()))
a.reverse()
print(sum(a[:k]))
