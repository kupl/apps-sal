l, r = list(map(int, input().split()))
c = l
print("YES")
while c < r:
    print(c, c + 1)
    c += 2
