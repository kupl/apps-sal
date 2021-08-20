N = int(input())
A = [int(input()) for _ in range(5)]
ans = -(-N // min(A)) + 4
print(ans)
