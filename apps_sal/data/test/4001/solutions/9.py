n = int(input())
a = list(map(int, input().split()))
x = max(a)
b = []
for i in range(1, x + 1) :
    if x % i == 0 :
        b.append(i)

for i in range(len(b)) :
    a.remove(b[i])

print(x, max(a))

