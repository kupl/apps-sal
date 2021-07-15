n,x = map(int,input().split())
lst = [int(input()) for _ in range(n)]

mini = min(lst)
re = x - sum(lst)
print(n + re // mini)
