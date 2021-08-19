def input_array():
    return list(map(int, input().split()))


n = int(input())
v = input_array()
v = sorted(v)
ans = v[0]
for i in range(1, n):
    ans = (ans + v[i]) / 2
print(ans)
