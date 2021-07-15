a = int(input())
b = [int(i) for i in input().split()]
c = [0] * 101
for elem in b:
    c[elem] += 1
print(max(c))

