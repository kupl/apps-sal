t = int(input())
for i in range(t):
    a, b, p = list(map(int, input().split()))
    s = input()
    n = len(s)
    ind = n
    sum = 0
    while sum <= p and ind > 0:
        ind -= 1
        if ind == n - 1 or s[ind - 1] != s[ind]:
            if s[ind - 1] == "A":
                sum += a
            else:
                sum += b
    print(ind + 1)
