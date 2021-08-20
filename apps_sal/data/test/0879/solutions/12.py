n = int(input())
l = input().split(' ')
l = [int(x) for x in l]
route = []
route.append(n)
current = l[-1]
while True:
    route.append(current)
    if current == 1:
        break
    current = l[current - 2]
for i in range(len(route)):
    print(route[len(route) - i - 1], end=' ')
