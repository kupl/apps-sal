n = int(input())
l = list(map(int, input().split()))
for i in range(1, n):
    if not l[i] - l[i - 1] == l[1] - l[0]:
        print(l[n - 1])
        break
else:
    print(l[n - 1] + l[1] - l[0])
