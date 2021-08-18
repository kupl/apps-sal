n, k = map(int, input().split())
if(n == k):
    print("1" * n)
    return
a = (n - k) >> 1
i = 0
Ans = ""
while(i < n):
    Ans += "0" * (a)
    i += a
    if(i > n - 1):
        break
    Ans += "1"
    i += 1
    if(i > n - 1):
        break
print(Ans[:n])
