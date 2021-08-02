q = int(input())

for _ in range(q):
    n = int(input())
    cnt = {'0': 0, '1': 0}
    even = []
    odd = []
    for _ in range(n):
        s = input()
        if len(s) & 1:
            odd.append(len(s))
        else:
            even.append(len(s))
        cnt['0'] += s.count('0')
        cnt['1'] += s.count('1')
    ans = n
    if cnt['0'] & 1 and cnt['1'] & 1 and len(odd) == 0:
        ans = n - 1
    print(ans)
