n, k = input().split()
n = int(n)
k = int(k)
s = input().split()
for i in range(n):
    s[i] = int(s[i])
    # print(i,"",end="")
r = (n - k) * 2
m = s[-1]
i = 0
if(k >= n):
    print(m)
else:
    while(i < r):
        x = s[i] + s[r - i - 1]
        # print(i,r-i)
        if(m < x):
            m = x
        i += 1
    print(m)
