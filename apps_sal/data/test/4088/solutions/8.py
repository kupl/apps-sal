from collections import Counter
q = int(input())
for _ in range(q):
    s = input()
    m = int(input())
    b = list(map(int, input().split()))
    c = Counter(s)
    c = list(c.items())
    c.sort(key=lambda x: x[0])

    ans = [None for _ in range(m)]
    while not all(ans):
        indices = []
        for i in range(m):
            if b[i] == 0:
                indices.append(i)
                b[i] = -1
        while True:
            if c[-1][1] >= len(indices):
                for idx in indices:
                    ans[idx] = c[-1][0]
                c.pop()
                break
            else:
                c.pop()
            
        for j in range(m):
            for idx in indices:
                b[j] -= abs(idx-j)
    print(''.join(map(str, ans)))
        

