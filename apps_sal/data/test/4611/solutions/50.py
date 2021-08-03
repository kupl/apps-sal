N = int(input())
T = [0, 0, 0]
ans = "Yes"
for _ in range(N):
    t = list(map(int, input().split()))
    k = abs((t[1] + t[2]) - (T[1] + T[2]))
    n = t[0] - T[0]
    if n % 2 == 0:
        if k > n or k % 2 != 0:
            ans = "No"
    else:
        if k > n or k % 2 == 0:
            ans = "No"
    T = t

print(ans)
