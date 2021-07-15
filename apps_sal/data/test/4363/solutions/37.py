K, S = list(map(int, input().split()))
c = 0

for x in range(K+1):
    for y in range(K+1):
        if 0 <= S-(x+y) <= K:
            c += 1
print(c)

