(A, B) = list(map(int, input().split()))
ans = [str(A) * B, str(B) * A]
ans.sort()
print(ans[0])
