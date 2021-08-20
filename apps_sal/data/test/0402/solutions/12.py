(n, k) = list(map(int, input().split()))
rem = 240
rem -= k
z = 5
ans = 0
while n > 0 and rem - z >= 0:
    rem -= z
    ans += 1
    n -= 1
    z += 5
print(ans)
