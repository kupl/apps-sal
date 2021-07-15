n = int(input())

males = [0]*368
females = [0]*368
for i in range(n):
    pol, a, b = input().split()
    a = int(a)
    b = int(b)
    if pol == 'M':
        for i in range(a,b+1):
            males[i]+=1
    else:
        for i in range(a,b+1):
            females[i]+=1
ans = 0
for i in range(368):
    if min(males[i],females[i])>ans:
        ans = min(males[i],females[i])
print(ans*2)
