(N, X) = list(map(int, input().split()))
li = list(map(int, input().split()))
d = 0
c = 1
for i in range(N):
    d = d + li[i]
    if d <= X:
        c = c + 1
print(c)
