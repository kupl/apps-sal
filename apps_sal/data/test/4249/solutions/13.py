import sys
n, m = list(map(int, input().split()))
l = list(map(int, input().split()))
l.sort(reverse=True)

left = 1
right = n + 1

ans = 10**18 + 1
while left != right:
    mid = (left + right) // 2
    # print(mid,left,right)
    din = 0
    kaam = 0
    c = 0
    for i in l:
        if i - din <= 0:
            break
        kaam += i - din
        c += 1
        if c == mid:
            c = 0
            din += 1
    if kaam >= m:
        ans = min(ans, mid)
        right = mid
    else:
        left = mid + 1

if ans == 10**18 + 1:
    print(-1)
else:
    print(ans)
'''
import sys
n = int(input())
l = list(map(int,input().split()))

freq = [0]*1001

for i in range(n*n):
    freq[l[i]] += 1

odd = oc = 0
two = []
print(freq[:11])
if n > 2:
    mn = 4
    
    for i in range(1001):
        if freq[i] != 0:
            
            if freq[i]%2 == 1:
                odd = i
                oc += 1
                freq[i] -= 1
            if freq[i]%2 == 0 and freq[i]%4 != 0:
                two.append(i)
                freq[i] -= freq[i]%4
                continue
                
            if freq[i]%4 != 0:
                print('NO')
                return
                
ans = [ [0]*n for i in range(n) ]

if not n%2 and odd != 0:
    print('NO')
    return


if oc > 1:
    print('NO')
    return
    
if n%2:
    ans[n//2][n//2] = odd

r = c = 0

print(two)
print(freq[:11])
mid = 0
for i in range(n):
    for j in range(n):
        if ans[i][j] == 0:
            for k in range(1,1001):
                if freq[k] != 0:
                    temp = k
                    r = i
                    c = j

                    ans[r][c] = ans[n-1-r][c] = ans[r][n-1-c] = ans[n-1-r][n-1-c] = temp
                    flag = False
                    if n%2 and ( n//2 == i or n//2 == j):
                        #print('are ye to odd hai')
                        if len(two) != 0:
                            ans[n//2][mid] = ans[n//2][n-mid-1] = two[-1]
                            flag = True
                            two.pop()
                        else:
                            ans[n//2][mid] = ans[n//2][n-mid-1] = temp
                        mid+=1
                    #print(freq[:7])
                    if not flag:
                        freq[k] =freq[k] - 4
                    else:
                        freq[k] = freq[k] - 2
                    #print(freq[:7])
                    break
print("YES")
for i in range(n):
    print(*ans[i])
'''
