n, m = list(map(int, input().split()))
bts = list(map(int, input().split()))

done = [0 for x in range(n)]

for i in bts:
    for j in range(i - 1, n):
        if done[j] == 0:
            done[j] = i

[print(x, end=' ') for x in done]
print()
