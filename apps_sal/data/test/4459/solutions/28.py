N = int(input())
A = list(map(int, input().split()))
ans = 0
dict = {}
for i in range(N):
    if A[i] in dict:
        dict[A[i]] += 1
    else:
        dict[A[i]] = 1
for x in dict:
    if x > dict[x]:
        ans += dict[x]
    else:
        ans += dict[x] - x
print(ans)
