from collections import Counter
n = int(input())
a = list(map(int,input().split()))
q = int(input())
bc = [list(map(int,input().split())) for _ in range(q)]
count = dict(Counter(a))
ans = sum(a)
for i in bc:
    try:
        ans += count[i[0]] * (i[1] - i[0])
        try:
            count[i[1]] += count[i[0]]
        except:
            count[i[1]] = count[i[0]]
        count[i[0]] = 0
        print(ans)
    except KeyError:
        print(ans)
        continue
