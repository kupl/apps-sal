N = int(input())
v = list(map(int, input().split()))
v.sort()
ans = v[0]

for i in range(N-1):
    ans = (ans+v[i+1]) / 2

# if str(ans)[-2:] == '.0':
#     print(str(ans).rstrip('.0'))
# else:
#     print(ans)

print(ans)
