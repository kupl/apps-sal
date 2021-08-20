(n, k, q) = map(int, input().split())
a = [int(input()) for i in range(q)]
ans = []


def calc(n):
    return n - q


for i in range(n):
    ans.append(k)
ans = list(map(calc, ans))
for i in range(q):
    ans[a[i] - 1] += 1
for i in range(n):
    if ans[i] <= 0:
        print('No')
    else:
        print('Yes')
