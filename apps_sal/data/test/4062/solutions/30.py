l = list(map(int, open(0).read().split()))
ans = [l[0] * l[2], l[0] * l[3], l[1] * l[2], l[1] * l[3]]
print(max(ans))
