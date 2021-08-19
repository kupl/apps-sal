a = int(input())
b = input().split()
b = [int(j) for j in b]
x = round(sum(b) / a)
y = []
for i in range(a):
    y.append((x - b[i]) ** 2)
print(sum(y))
