n, k, q = map(int, input().split())
l = [0]*n
for i in range(q):
    l[int(input()) - 1] += 1
for j in range(n):
    if l[j] > q-k:
        print("Yes")
    else:
        print("No")
