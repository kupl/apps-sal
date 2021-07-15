K = int(input())

ans = list(range(50))[::-1]
q, r = divmod(K, 50)

for i in range(50):
    ans[i] += q
for i in range(r):
    ans[i] += 1

print((len(ans)))
print((*ans))

