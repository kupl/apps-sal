n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))
a.sort(reverse=True)
s = sum(a)
for i in range(m):
    print(s - a[q[i] - 1])



