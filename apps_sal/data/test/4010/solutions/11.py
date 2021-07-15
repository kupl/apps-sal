def go():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i, aa in enumerate(a):
        if aa in d:
            if i - d[aa] > 1 :
                return 'YES'
        d[aa] = d.get(aa, i)
    return 'NO'


t = int(input())
for _ in range(t):
    print(go())

