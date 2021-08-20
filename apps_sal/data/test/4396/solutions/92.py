n = int(input())
x = []
for i in range(n):
    (a, b) = input().split()
    if b == 'JPY':
        x.append(int(a))
    else:
        x.append(float(a) * 380000)
print(sum(x))
