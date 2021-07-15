n, d = [int(x) for x in input().split()]
s = list(map(int, input().split()))
l = list(map(int, input().split()))
score = s[d - 1] + l[0]
rank = d
j = n - 1
for i in range(d - 1):
    if s[i] <= score:
        if s[i] + l[j] <= score:
            rank -= 1
            j -= 1
print(rank)
