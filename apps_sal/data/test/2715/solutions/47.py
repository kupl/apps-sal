K = int(input())

q, r = divmod(K, 50)

ans = [i + q for i in range(50)]
for i in range(1, r + 1):
    ans[-i] += 1

print((50))
print((*ans))

