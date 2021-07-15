from math import ceil
n, m = list(map(int, input().split()))
s1 = ""
s2 = ""
if not (n-1 <= m and m <= 2 * (n+1)):
    print(-1)
elif m == n-1:
    print("01"*m+"0")
elif m == n:
    print("10"*m)
else:
    s1 = "10"*n+"1"
    for i in s1:
        s2 += i
        if i == "1" and m-n-1:
            s2 += "1"
            m -= 1
    print(s2)

