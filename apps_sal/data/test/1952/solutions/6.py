(n, k) = list(map(int, input().split()))
m = list(map(int, input().split()))
c = list(map(int, input().split()))
num = [0] * (k + 1)
for i in m:
    num[i] += 1
for i in range(k - 1, -1, -1):
    num[i] += num[i + 1]
num = num[1:]
maxi = 0
for i in range(k):
    maxi = max((num[i] - 1) // c[i] + 1, maxi)
ans = [[] for i in range(maxi)]
m.sort(reverse=True)
for i in range(len(m)):
    ans[i % maxi].append(m[i])
print(len(ans))
for i in range(maxi):
    print(' '.join(map(str, [len(ans[i])] + ans[i])))
