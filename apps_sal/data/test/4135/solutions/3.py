n = int(input())
a = list(input().strip())
i = 1
while(i <= n):
    if(n % i == 0):
        a = a[:i][::-1] + a[i:]
    i += 1
print("".join(a))
