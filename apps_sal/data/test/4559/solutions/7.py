n = int(input())
l = list(map(int, input().split()))
# print(l)
ans = 1
if 0 in l:
    print(0)
    return
for i in l:
    ans *= i
    if ans > 10**18:
        # print(ans)
        print(-1)
        return
print(ans)
