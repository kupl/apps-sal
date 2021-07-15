import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))
set_ = set([]) 
set_2 = set([])
ans = []


for i in range(n):
    if a[i] > 0:
        if a[i] not in set_2:
            set_.add(a[i])
        else:
            print(-1)
            return
        set_2.add(a[i])
    else:
        if abs(a[i]) in set_:
            set_.remove(-a[i])
        else:
            print(-1)
            return

    if not set_:
        set_2 = set([])
        ans.append(i+1)

if set_:
    print(-1)
    return
    
res = [0]*len(ans)
for i in range(len(ans)):
    if i == 0:
        res[i] = ans[i]
    else:
        res[i] = ans[i] - ans[i-1]
print(len(res))
print(*res)
