(N, M) = list(map(int, input().split()))
ans = set(list(map(int, input().split()))[1:])
for i in range(N - 1):
    line = set(list(map(int, input().split()))[1:])
    ans = ans & line
print(len(ans))
