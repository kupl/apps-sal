s = input()
k = int(input())
lst = sorted(list(set(s)))
tank = []
for tg in lst:
    for i in range(len(s)):
        if s[i]==tg:
            for j in range(k):
                if i+j<=len(s) and (s[i:i+j+1] not in tank):
                    tank.append(s[i:i+j+1])
    if len(tank) >= k:
        break
tank.sort()
print(tank[k-1])
