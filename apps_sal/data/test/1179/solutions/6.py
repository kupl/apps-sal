n, k = map(int, input().split())
c, id = 1, list(map(int, input().split()))
while k > c:
    k, c = k - c, c + 1
print(id[k - 1])
