N, X = map(int, input().split())

ex = [False] * 2 ** 18
ex[0] = True
ans = [0]

for i in range(1, 2 ** N):
    if ex[i ^ X]:
        continue
    else:
        ans.append(i)
        ex[i] = True

print(len(ans) - 1)
for i in range(1, len(ans)):
    print(ans[i] ^ ans[i - 1], end=" ")
