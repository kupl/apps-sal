n = int(input())
m = list(map(int, input().split()))
r = list(map(int, input().split()))
count = 0
N = 100000
for D in range(N):
    for i in range(n):
        if D % m[i] == r[i]:
            count += 1
            break
print(count / N)
