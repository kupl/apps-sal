(A, B) = map(int, input().split())
ans = 0
for i in range(10, 1001):
    if int(i * 0.08) == A and int(i * 0.1) == B:
        ans = i
        break
if ans == 0:
    print(-1)
else:
    print(i)
