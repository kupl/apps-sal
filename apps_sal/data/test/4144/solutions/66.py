N = int(input())
if N == 1:
    print(0)
    return
ans = 10**N - 9**N - 9**N + 8**N
print(ans%(10**9+7))
