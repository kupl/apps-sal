N = int(input())
(*L,) = map(int, input().split())
L.sort()
ans = sum((L[2 * i] for i in range(N)))
print(ans)
