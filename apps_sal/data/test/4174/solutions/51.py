N, X = map(int, input().split())
L = list(map(int, input().split()))

bound = 1
d = 0
for i in L:
    d += i
    if d <= X:
        bound += 1
print(bound)
