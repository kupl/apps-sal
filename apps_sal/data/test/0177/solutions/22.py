x = []
for i in range(1,10001):
    x.append(str(i))
x = "".join(x)
k = int(input())
print(x[k-1])

