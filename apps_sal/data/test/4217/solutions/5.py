n, m = list(map(int, input().split()))
like = [0]*m

for _ in range(n):
    al = list(map(int, input().split()))
    arr = al[1:]
    for a in arr:
        like[a-1] += 1

print((like.count(n)))

