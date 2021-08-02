n = int(input())
A = list(map(int, input().split()))
b = input()
ans = 0
per = 0
start = 0
for i in range(n):
    if b[i] == 'B':
        start += A[i]
for i in range(n):
    if b[i] == 'A':
        per += A[i]
    else:
        per -= A[i]
    ans = max(per, ans)

per = 0
for i in range(n - 1, -1, -1):
    if b[i] == 'A':
        per += A[i]
    else:
        per -= A[i]
    ans = max(per, ans)
print(start + ans)
