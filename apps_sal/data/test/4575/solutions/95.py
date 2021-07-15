def LI():
    return list(map(int, input().split()))


N = int(input())
D, X = LI()
ans = X
for _ in range(N):
    A = int(input())
    for i in range(100):
        if A*i+1 <= D:
            ans += 1
            continue
        break
print(ans)

