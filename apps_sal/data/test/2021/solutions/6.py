n = int(input())
u = list(map(int, input().split()))
k = int(input())
a = list(map(int, input().split()))
u.sort(reverse = 1)
s = sum(u)
for i in range(k):
    print(s - u[a[i] - 1])

