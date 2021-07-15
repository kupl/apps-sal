n = int(input())
arr = list(map(int,input().split()))
ans = 0
counter = [0] * 6
d = {4:0,8:1,15:2,16:3,23:4,42:5}

for a in arr:
    index = d[a]
    counter[index] += 1
    if index > 0 and counter[index] > counter[index-1]:
        counter[index] -= 1
        ans += 1
        
ans += sum(counter) - counter[5] * 6

print(ans)

