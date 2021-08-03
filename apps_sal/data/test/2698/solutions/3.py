def ans(dic, v):
    count = 0
    for i in range(1, 3002):
        try:
            k = dic[i - 1]
            l = v - k
            if k <= v:
                count += k
                if l > dic[i]:
                    count += dic[i]
                    dic[i] = 0
                else:
                    count += l
                    dic[i] -= l
            else:
                count += v
        except:
            continue
    return count


m, v = [int(x) for x in input().split()]
dic = {i: 0 for i in range(3002)}
for i in range(m):
    try:
        d, a = [int(x) for x in input().split()]
        dic[d] += a
    except:
        continue
print(ans(dic, v))
