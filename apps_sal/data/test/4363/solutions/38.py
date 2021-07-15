# B - Sum of Three Integers

k,s = list(map(int,input().split()))
c = 0
min_limit = s - k

for i in range(k+1):
    for j in range(k+1):
        if i + j <= s and i + j >= min_limit:
            c += 1
print(c)

