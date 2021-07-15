def generate(made, lis):
    if made == n:
        nonlocal res
        s = sum(lis)
        if l <= s and s <= r and len(lis) >= 2 and lis[-1] - lis[0] >= x:
            res += 1
    else:
        generate(made + 1, lis + [a[made]])
        generate(made + 1, lis)

n, l, r, x = list(map(int, input().split()))
a = sorted(map(int, input().split()))
res = 0
generate(0, [])
print(res)

