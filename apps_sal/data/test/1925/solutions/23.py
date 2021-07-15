A, B, N = map(int, input().split())
ans = (A*min(N, B-1))//B
print(ans)
