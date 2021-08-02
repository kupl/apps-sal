A, B = map(int, input().split())

ans = [A + B, A - B, A * B]
print(max(ans))
