import sys

n = int(input())
a = list(map(int, input().split()))

d = dict()

for elem in a:
    d[elem] = d.get(elem, 0) + 1

not_uniq = 0
for elem in d:
    if d[elem] > 1:
        not_uniq += 1

if not_uniq == 0:
    print(0)
    return

ans = 10 ** 9
left = 0
right = -1

while True:
    if not_uniq == 0:
        ans = min(ans, right - left + 1)
    if not_uniq > 0:
        right += 1
        if right >= n:
            break
        elem = a[right]
        d[elem] -= 1
        if d[elem] == 1:
            not_uniq -= 1
    else:
        elem = a[left]
        d[elem] += 1
        if d[elem] == 2:
            not_uniq += 1
        left += 1

print(ans)


        
    

