N = input()
n = int(N)
ans = 0

if(len(N) == 1):
    print(n)
    return
if(len(N) % 2 == 1):
    ans += n - (10 ** (len(N)-1)) + 1
    n -= ans
    for i in range(1,len(str(n))+1):
        if(i % 2 == 1):
            ans += 9 * (10 ** (i - 1))
    print(ans)
else:
    n -= n - (10 ** (len(N)-1)) + 1
    for i in range(1,len(str(n))+1):
        if(i % 2 == 1):
            ans += 9 * (10 ** (i - 1))
    print(ans)
