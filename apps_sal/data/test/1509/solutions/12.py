def in_int():
    return int(input())


def in_list():
    return [int(x) for x in input().split()]


n = in_int()
ns = in_list()

ans = 0
for i in range(n - 1):
    # a=min(ns[i],ns[i+1])
    # b=max(ns[i],ns[i+1])
    a, b = ns[i], ns[i + 1]
    if a > b:
        ans += (a - b) * (n - a + 1)
    else:
        ans += a * (b - a)
    # print(ans)
    # ans+=a*(b-a)
    # ans+=(n-b+1)*(b-a)
    # print(ans)
a = ns[-1]
ans += a * (n - a + 1)
# print(ans)
# ans+=n*(n+1)//2
print(ans)

# 2 1 3
# 1 2 3 4 5 6 7
# 3 5
