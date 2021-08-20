X = int(input())
max_expo = 1
for p in range(2, 10):
    for b in range(X):
        if max_expo < b ** p <= X:
            max_expo = b ** p
print(max_expo)
