(A, B, C) = map(int, input().split())
ans = C if C < B // A else B // A
print(ans)
