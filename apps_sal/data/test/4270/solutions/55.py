N = int(input())
v = list(map(int, input().split()))
v = sorted(v)
result = v[0]
for i in range(1, len(v)):
    result = (result + v[i]) / 2
print(result)
