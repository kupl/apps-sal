q = int(input())
for _ in range(q):
    s = input()
    n = len(s)
    pref = [0] * n
    pref[0] = 1
    if s[0] == '-':
        pref[0] = -1
    for i in range(1,n):
        pref[i] = pref[i-1] + (1 if s[i] == '+' else -1)
    pierszyminus = [-1]*(n+1)
    for i in range(n):
        j = n-1-i
        if pref[j] < 0:
            pierszyminus[-pref[j]] = j
    wyn = 0
    for i in range(1,n+1):
        wyn += (pierszyminus[i]+1)
    wyn += n
    print(wyn)
