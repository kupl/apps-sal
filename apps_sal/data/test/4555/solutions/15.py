(A, B, K) = map(int, input().split())
ans = []
for i in range(K):
    if A + i <= B and A + i not in ans:
        ans.append(A + i)
    if B - i >= A and B - i not in ans:
        ans.append(B - i)
ans.sort()
for i in ans:
    print(i)
