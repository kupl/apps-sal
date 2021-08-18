import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))

if n < k:
    print("NO")
    return

LIST = [[] for i in range(max(A) + 1)]

for i in range(n):
    LIST[A[i]].append(i)

for li in LIST:
    if len(li) > k:
        print("NO")
        return


ANS = [None] * n

i = 1
for li in LIST:
    for num in li:
        ANS[num] = i
        i += 1
        if i == k + 1:
            i = 1


print("YES")
for a in ANS:
    print(a, end=" ")
