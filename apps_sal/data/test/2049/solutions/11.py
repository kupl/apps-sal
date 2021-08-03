import sys
input = sys.stdin.readline
a, b = list(map(int, input().split()))
z = list(map(int, input().split()))
ans = [0]
for i in range(1, len(z)):
    if(z[i] > z[i - 1]):
        ans.append(1)
    elif(z[i] < z[i - 1]):
        ans.append(2)
    else:
        ans.append(0)

start = [0 for i in range(len(ans))]
for i in range(len(ans) - 1, -1, -1):
    if(ans[i] == 2):
        start[i] = i
    else:
        if(i == len(ans) - 1):
            start[i] = -1
        else:
            start[i] = start[i + 1]
end = [0 for i in range(len(ans))]
for i in range(len(ans)):
    if(ans[i] == 1):
        end[i] = i
    else:
        if(i == 0):
            end[i] = -1
        else:
            end[i] = end[i - 1]

for i in range(b):
    l, r = list(map(int, input().split()))
    if(l == len(z)):
        print('Yes')
        continue
    if(start[l] == -1 or end[r - 1] == -1):
        print('Yes')
    else:
        if(start[l] > end[r - 1]):
            print('Yes')
        else:
            print('No')
