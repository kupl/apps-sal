a = int(input())
l = list(map(int, input().split()))
ans = [0 for i in range(100)]
for i in l:
    n = 0
    while i % 2 == 0:
        n += 1
        i //= 2
    ans[n] += 1
k = ans.index(max(ans))
ann = []
for i in l:
    if i % (2 ** k) != 0 or i % (2 ** (k + 1)) == 0:
        ann.append(i)
    else:
        pass
print(len(ann))
print(*ann)
