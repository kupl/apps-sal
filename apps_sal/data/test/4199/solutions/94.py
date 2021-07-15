n,k = map(int, input().split())
h = map(int, input().split())
print(len([i for i in h if i >= k]))
