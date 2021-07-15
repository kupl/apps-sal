N = int(input())

if N % 2 == 0:
    ans = 0.5
else:
    ans = (N//2 + 1)/N

print(ans)
