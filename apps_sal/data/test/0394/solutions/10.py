n = int(input())
a = [0] + [int(i) for i in input().split()]
d = [a[i] - a[i-1] for i in range(1, n+1)]
ans = []
for i in range(1, n+1):
    if (d[:i] * (n//i + 20))[:n] == d:
        ans.append(i)
print(len(ans))
print(' '.join([str(i) for i in ans]))

