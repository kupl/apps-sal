import collections
N = int(input())
A = list(map(int, input().split()))
A = collections.Counter(A).most_common()
N = len(A)
ans = [0]
for i in range(N):
    if A[i][1] >= 4:
        ans.append(A[i][0] ** 2)
ref = []
for j in range(N):
    if A[j][1] >= 2:
        ref.append(A[j][0])
ref = sorted(ref)
if len(ref) >= 2:
    ans.append(ref[-2] * ref[-1])
print(max(ans))
