INF = 10 ** 9 + 7
N = int(input())
H = list(map(int, input().split()))
H.append(INF)
ans = 'Yes'
for i in reversed(range(N)):
    if not H[i] <= H[i + 1]:
        H[i] -= 1
    if not H[i] <= H[i + 1]:
        ans = 'No'
        break
print(ans)
