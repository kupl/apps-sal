(N, A, B) = map(int, input().split())
ans = 0
for n in range(1, N + 1):
    if A <= sum(list(map(int, list(str(n))))) <= B:
        ans += n
print(ans)
