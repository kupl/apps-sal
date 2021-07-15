n=int(input())
for i in range(n):
    s=input()
    t=input()
    s1 = set()
    s2=set()
    for q in s:
        s1.add(q)
    for q in t:
        s2.add(q)
    if len(s1.intersection(s2)):
        print('YES')
    else:
        print('NO')
