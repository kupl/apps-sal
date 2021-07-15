t = int(input())
for i in range(t):
    n = input()
    ans = (len(n) - 1) * 9
    for j in range(1, 10):
        if n >= str(j) * len(n):
            ans += 1
    print(ans)
