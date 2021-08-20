N = int(input())
ans = N
for i in range(int(N ** 0.5) + 1, 1, -1):
    if N % i == 0:
        ans = N // i
        break
print(len(str(ans)))
