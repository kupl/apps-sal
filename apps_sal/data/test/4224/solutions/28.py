n = int(input())
a = list(map(int, input().split()))
lst = []
for i in a:
    if i % 2 == 0:
        lst.append(i)


def half(x):
    cnt = 0
    for i in range(x):
        if x % 2 == 0:
            x = x // 2
            cnt += 1
        else:
            break
    return cnt


ans = 0
for i in lst:
    ans += half(i)
print(ans)
