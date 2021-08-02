import collections
N = int(input())
ls = [0] + [0] * N
couterls = collections.Counter(ls)
for i in range(1, N + 1):
    for j in range(2, N + 1):
        if i % j == 0:
            while i % j == 0:
                couterls[j] += 1
                i = i // j
        elif i == 1:
            break
        else:
            pass
ans = 1
couterls.pop(0)
for i in couterls.values():
    ans = (ans * (i + 1)) % (10**9 + 7)
print(ans)
