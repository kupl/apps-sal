def ans135(N: int, p: str):
    p = list(map(int, p.split()))
    psort = sorted(p)
    if p == psort:
        return 'YES'
    else:
        count = 0
        for i in range(len(p)):
            if p[i] != psort[i]:
                count += 1
        if count == 2:
            return 'YES'
        else:
            return 'NO'


N = int(input())
p = input()
print(ans135(N, p))
