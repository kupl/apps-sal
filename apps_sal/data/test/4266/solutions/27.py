
k, x = list(map(int, input().split()))
b = []


for i in range(x - k + 1, x + k):

    b.append(str(i))

b = " ".join(b)

print(b)
