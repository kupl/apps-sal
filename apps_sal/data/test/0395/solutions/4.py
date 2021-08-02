import sys
t = list(map(int, input().split()))
for i in range(6):
    for j in range(6):
        for m in range(6):
            if i != m and i != j and j != m:
                s = t[i] + t[j] + t[m]
                if(s * 2 == sum(t)):
                    print('YES')
                    return
print('NO')
