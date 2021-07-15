n, m = list(map(int, input().split()))
like = [0]*m
for _ in range(n):
    al = list(map(int, input().split()))
    k = al[0]
    ai = al[1:]
    for a in ai:
        like[a-1] += 1

print((like.count(n)))

