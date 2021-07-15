n = int(input())

s = input()

if n % 2 == 1:
    print("No")
else:
    n = n // 2
    ans = 0
    for i in range(n):
        if s[:n] == s[n:]:
            ans += 1
    if ans == n:
        print("Yes")
    else:
        print("No")
