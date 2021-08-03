n, k, q = map(int, input().split())
a = []
for i in range(q):
    A = int(input())
    a.append(A)
ans = [0] * n
for i in range(q):
    ans[a[i] - 1] += 1
for i in range(n):
    if q - k + 1 <= ans[i]:
        print("Yes")
    else:
        print("No")
