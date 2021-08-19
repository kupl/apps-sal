n = int(input())
A = list(map(int, input().split()))
ans = 0
E = {}
for i in range(n):
    if A[i] == i:
        ans += 1
    else:
        E[i] = A[i]
done = False
for item in E:
    if E[E[item]] == item:
        ans += 2
        done = True
        break
if not done and len(E) > 0:
    ans += 1
print(ans)
