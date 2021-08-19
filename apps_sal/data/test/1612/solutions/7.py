n = int(input())
(s, t) = (['YES'] * n, [set(map(int, input().split()[1:])) for i in range(n)])
for i in range(n):
    for j in range(n):
        if i != j and t[i].issuperset(t[j]):
            s[i] = 'NO'
            break
print('\n'.join(s))
