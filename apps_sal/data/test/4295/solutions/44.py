(N, Y) = map(int, input().split())
ans = min(N % Y, Y - N % Y)
print(ans)
