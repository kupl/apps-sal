n = int(input())
v = list(map(int, input().split()))

ret = max(v)
idx = v.index(ret)
v[idx] = -1
ret = max(v)

print(str(idx + 1) + ' ' + str(ret))
