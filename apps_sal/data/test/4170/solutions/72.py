N = int(input())
H = [int(x) for x in input().split()]
ans = 0
num = 0
for i in range(N - 1):
    if(H[i] >= H[i + 1]):
        num += 1
    else:
        ans = max(ans, num)
        num = 0
ans = max(ans, num)
print(ans)
