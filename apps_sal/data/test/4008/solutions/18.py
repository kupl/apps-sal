n,k = [int(e) for e in input().strip().split()]
num = [int(e) for e in input().strip().split()]

count = dict()
valid = True

for i in range(n):
    if num[i] not in count:
        count[num[i]] = 0
    count[num[i]] += 1
    if count[num[i]] > k:
        valid = False

if not valid:
    print("NO")
else:
    out = ""
    color = dict()
    for i in range(k):
        color[i] = set()
    now_color = 0
    for a in num:
        while True:
            if a in color[now_color]:
                now_color += 1
                now_color %= k
                continue
            else:
                out += str(now_color+1) + " "
                color[now_color].add(a)
                now_color += 1
                now_color %= k
                break
    out = out.strip()
    print("YES")
    print(out)

