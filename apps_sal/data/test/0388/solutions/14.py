def solve(n, k, a):
    t = 0
    ans = ["" for i in range(n)] 
    
    i = 0
    while ((i < len(a)) and (a[i] == 'NO')):
        ans[i] = names[0]
        i += 1
    
    if (i == len(a)):
        for j in range(i, i + k - 1):
            ans[j] = ans[0]
        return(ans)
    
    for j in range(i, i + k):
        ans[j] = names[t]
        t += 1
    
    while (i < len(a)):
        if (a[i] == 'NO'):
            ans[i + k - 1] = ans[i]
        else:
            ans[i + k - 1] = names[t]
            t += 1
        i += 1

    return ans 




names = []
for i in range(ord('A'), ord('Z')+ 1):
    for j in range(ord('a'), ord('z')+ 1):
        names.append(chr(i) + chr(j))
'''
import random
for i in range(100000):
    n = random.randint(2, 52)
    k = random.randint(2, n)
    a = [random.choice(['YES', 'NO']) for i in range(n - k)]
    ans = solve(n, k, a)
    for i in range(0, n - k):
        s = set(ans[i:i+k])
        is_diff = len(s) == k
        if (a[i] == 'YES'):
            if (len(s) != k):
                print(n, k)
                print(a)
                print(ans)
                exit
        if (a[i] == 'NO'):
            if (len(s) == k):
                print(n, k)
                print(a)
                print(ans)
                exit
'''     
n, k = list(map(int, input().strip().split()))
is_ok = input().strip().split()
ans = solve(n, k, is_ok)
print(*ans)


