t = int(input())
answer = []

def mini(arr):
    minimum = arr[0]
    index = 0
    for i in range (1, len(arr)):
        if minimum > arr[i]:
            minimum = arr[i]
            index = i
    return index

for i in range (t):
    n = int(input())
    p = list(map(int,input().split()))
    ans = []
    
    while len(p) > 1:
        index = mini(p)
        ans.append(p[index])
        for k in range (index - 1):
            ans.append(p[k])
        p = p[index-1 : index] + p[index + 1:]
    if len(p) == 1:
        ans.append(p[0])
    answer.append(ans)
for i in range (t):
    print (*answer[i], sep = " ")
