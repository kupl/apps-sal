n, x = map(int, input().split())
l = list(map(int, input().split()))

d = [0]
for i in range(n):
    d.append(d[-1]+l[i])
print(len([i for i in d if i <= x]))
