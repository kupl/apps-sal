k = int(input())
rs = set(map(int, input().split(' ')))
for i in range(25 - k):
    for j in range(1, 10000000):
        if j not in rs:
            rs.add(j)
            break
print(max(rs) - 25)
