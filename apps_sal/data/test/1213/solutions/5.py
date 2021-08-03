import sys
n, k = list(map(int, input().split()))

s = input()

k -= 1

Ans = ""

if((k + 1) > n // 2):
    for j in range(k, n - 1):
        Ans += "PRINT " + s[j] + "\n"
        Ans += "RIGHT\n"
    Ans += "PRINT " + s[n - 1] + "\n"
    ind = n - 1
    if(k > 0):
        while(ind >= k):
            Ans += "LEFT\n"
            ind -= 1
        for i in range(ind, 0, -1):
            Ans += "PRINT " + s[i] + "\n"
            Ans += "LEFT\n"
        Ans += "PRINT " + s[0] + "\n"

else:
    for j in range(k, 0, -1):
        Ans += "PRINT " + s[j] + "\n"
        Ans += "LEFT\n"
    Ans += "PRINT " + s[0] + "\n"
    ind = 0
    if(k < n - 1):
        while(ind <= k):
            Ans += "RIGHT\n"
            ind += 1
        for i in range(ind, n - 1):
            Ans += "PRINT " + s[i] + "\n"
            Ans += "RIGHT\n"
        Ans += "PRINT " + s[n - 1] + "\n"
sys.stdout.write(Ans)
