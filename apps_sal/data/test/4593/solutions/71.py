X = int(input())
cnt = 1
for b in range(1, X):
    for p in range(2, X):
        if b ** p <= X:
            cnt = max(cnt, b ** p)
        else:
            break
print(cnt)
