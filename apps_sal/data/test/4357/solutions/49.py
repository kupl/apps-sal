val = list(map(int, input().split()))
val.sort(reverse=True)
print(val[0] * 10 + val[1] + val[2])
