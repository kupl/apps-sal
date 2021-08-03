n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def MAX(a):
    ans = -float('inf')
    for i in b:
        for j in a:
            ans = max(ans, i * j)
    return ans


max_ = {i: -float('inf') for i in range(len(a))}

for i in range(len(a)):
    new_a = a[:i] + a[i + 1:]
    max_[i] = MAX(new_a)

print(min(i for i in list(max_.values())))
