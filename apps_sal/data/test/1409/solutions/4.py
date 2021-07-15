n, k = list(map(int, input().split()))
g = list(map(int, input().split()))
r = 0
for i in g:
    if i <= 5-k:
        r+=1

print(r//3)

