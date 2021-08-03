n = int(input())
a = map(int, input().split())
b = []
for i in a:
    b.append(i - 1)
print(sum(b))
