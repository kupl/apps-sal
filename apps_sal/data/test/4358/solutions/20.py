N = int(input())
a = []
for _ in range(0, N):
    a.append(int(input()))

price=max(a)//2+sum(a)-max(a)

print(price)


