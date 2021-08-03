n = int(input())
books = [int(x) for x in input().split(' ')]
steps = [int(x) for x in input().split(' ')]

furthest_move = 0
d = {}
for i in range(n):
    d[books[i]] = i + 1
res = ""
for i in range(n):
    if d[steps[i]] > furthest_move:
        res += str(d[steps[i]] - furthest_move) + " "
        furthest_move = d[steps[i]]
    else:
        res += "0 "

print(res.strip())
