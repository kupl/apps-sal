X = int(input())
ans = []
ans.append(1)
for i in range(2, X):
    a = i * i
    while a <= X:
        ans.append(a)
        a *= i
print((max(ans)))
