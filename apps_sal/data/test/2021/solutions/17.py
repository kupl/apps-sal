n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))
a = sorted(a, key=lambda x: -x)
s = sum(a)
for i in range(m):
    ans = s - a[q[i] - 1]
    print(s - a[q[i] - 1])
