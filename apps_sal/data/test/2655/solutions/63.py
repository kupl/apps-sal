N = int(input())
A = list(map(int, input().split()))
B = []
for a in A:
    B.append(a)
    B.append(a)
B.sort()
B.pop()
ans = 0
for i in range(N - 1):
    ans += B.pop()
print(ans)
