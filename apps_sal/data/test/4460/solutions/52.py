x = list(map(int, input().split()))
a = 300
for i in range(len(x)):
    if x[i] == 0:
        a = i + 1
print(a)

