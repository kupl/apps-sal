H, W = list(map(int, input().split()))
N = int(input())
a = [int(x) for x in input().split()]
temp = []
for i in range(N):
    for _ in range(a[i]):
        temp.append(i + 1)
ans = []
for i in range(H):
    ans = temp[i * W:(i + 1) * W]
    if i & 1:
        ans.reverse()
    print((*ans))
