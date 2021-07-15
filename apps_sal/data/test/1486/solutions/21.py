n = int(input())
s = [int(i) for i in input().split()]
ans1 = [0]*n
ans2 = [2000000003]*n
for i in range(n):
        ans1[i] = max(abs(s[i]-s[0]),abs(s[i]-s[-1]))
        if i!=0 and i!= n-1:
            ans2[i] =  min(abs(s[i]-s[i+1]),abs(s[i]-s[i-1]))
        elif i == 0:
            ans2[i] = abs(s[0]-s[1])
        else:
            ans2[i] = abs(s[n-2]-s[n-1])
for i in range(n):
    print(ans2[i], ans1[i])

