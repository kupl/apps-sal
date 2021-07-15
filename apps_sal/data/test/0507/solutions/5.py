n = int(input())
ai = list(map(int,input().split()))
bi = list(map(int,input().split()))
ci = [0]*n
for i in range(n):
    ci[i] = ai[i]
nums = [0]*n
ind = [0]*2
j = 0
num = 0
for i in range(n):
    nums[ai[i]-1] += 1
for i in range(n):
    if nums[ai[i]-1] == 2:
        ind[j] = i
        j += 1
    if nums[i] == 0:
        num = i+1 
        
ci[ind[0]] = num
dif = 0
dif2 = 0
for i in range(n):
    if ci[i] != bi[i]:
        dif += 1
    if ci[i] != ai[i]:
        dif2 += 1
if dif != 1 or dif2 != 1:
    ci[ind[0]] = ai[ind[0]]
    ci[ind[1]] = num
for i in range(n):
    print(ci[i],end=" ")

