

t = int(input())

for _ in range(t):
    n = int(input())
    k = []
    for i in range(n):
        k.append(input())
    total = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if k[i] == k[j]:
                count += 1
        if count > 1:
            temp = k[i]
            for a in ['0','1','2','3','4','5','6','7','8','9']:
                if a + k[i][1:] not in k:
                    k[i] = a + k[i][1:]
                    break
            if temp == k[i]:
                for a in ['0','1','2','3','4','5','6','7','8','9']:
                    if k[i][0] + a + k[i][2:] not in k:
                        k[i] = a + k[i][1:]
                        break
            total += 1
    print(total)
    for i in range(n):
        print(k[i])

