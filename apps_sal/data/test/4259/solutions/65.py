K = int(input())
(A, B) = map(int, input().split())
ans = 'OK' if B // K - (A - 1) // K > 0 else 'NG'
print(ans)
