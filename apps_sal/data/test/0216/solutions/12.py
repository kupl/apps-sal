n = int(input())
a = list(map(int, input().split()))
b = [i for i in a if i < 0]
print(sum(a) - 2 * sum(b))

