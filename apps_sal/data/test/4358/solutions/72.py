a = int(input())
b = [int(input()) for i in range(a)]
b.sort()
b[len(b) - 1] = int(b[len(b) - 1] / 2)
print(sum(b))
