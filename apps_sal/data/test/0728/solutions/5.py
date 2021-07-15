def check(m, a):
    for i in range(1, len(a)):
        if a[i] >= m:
            return True
    return False

n = int(input())
a = list(map(int, input().split()))
ms = a[0]
ans = 0
while check(a[0], a):
    pos = a[1:].index(max(a)) + 1
    a[pos] -= 1
    a[0] += 1
    ans += 1
print(ans)

