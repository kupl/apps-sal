n, k = map(int, input().split())
a = list(map(int, input().split()))

n = n-k
if n%(k-1) == 0:
    print(n//(k-1)+1)
else:
    print(n//(k-1)+2)
