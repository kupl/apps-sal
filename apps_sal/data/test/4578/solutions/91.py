(n, x) = map(int, input().split())
li = []
for i in range(n):
    li.append(int(input()))
n1 = sum(li)
n2 = min(li)
n3 = len(li)
print(n3 + (x - n1) // n2)
