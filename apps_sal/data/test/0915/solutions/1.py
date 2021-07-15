import sys
readline = sys.stdin.readline
K = int(readline())

S = 'codeforces'

arr = [1]*10

for _ in range(1000):
    res = 1
    for a in arr:
        res *= a
    if res >= K:
        break
    arr[arr.index(min(arr))] += 1
    
    

ans = ''
for i in range(10):
    ans = ans + S[i]*arr[i]

print(ans)
