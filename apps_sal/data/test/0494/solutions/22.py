def main():
    n, m = [int(item) for item in input().split()]
    l = [int(item) for item in input().split()]
    l = [0] + l
    a = [0] * (n + 1)
    
    for i in range(1, m):
        curr = (l[i + 1] - l[i] - 1) % n + 1
        if a[l[i]] != 0 and curr != a[l[i]]:return -1
        a[l[i]] = curr
    #print(a)
    cnt = [0] * (n + 1)
        
    for i in range(1, n + 1):
        cnt[a[i]] += 1
        if a[i] != 0 and cnt[a[i]] > 1:
            return -1

    if cnt[0] != 0:
        d = []
        for k in range(1, n + 1):
            if cnt[k] == 0:
                d.append(k)
        for i in range(1, n + 1):
            if a[i] == 0:
                a[i] = d[0]
                d.pop(0)

    return " ".join(str(x) for x in a[1:])
    
print(main())
