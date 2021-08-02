n, k = list(map(int, input().split()))

a = list(input().split())

while not set(list(str(n)[0:k])).isdisjoint(a):
    n += 1

print(n)
