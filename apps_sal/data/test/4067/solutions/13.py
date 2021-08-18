n = int(input())
m = n // 3
a = list(input().strip())
a = list(map(int, a))
count = [0] * 3
for i in a:
    count[i] += 1
if(count[0] > m):
    i = c = 0
    while(c <= m):
        if(a[i] == 0):
            c += 1
        i += 1
    j = i - 1
    while(j < n and count[1] < m):
        if(a[j] == 0):
            a[j] = 1
            count[0] -= 1
            count[1] += 1
        j += 1
    if(count[0] > m):
        while(j < n and count[2] < m):
            if(a[j] == 0):
                a[j] = 2
                count[0] -= 1
                count[2] += 1
            j += 1
if(count[2] > m):
    i = n - 1
    c = 0
    while(c <= m):
        if(a[i] == 2):
            c += 1
        i -= 1
    j = i + 1
    while(j >= 0 and count[1] < m):
        if(a[j] == 2):
            a[j] = 1
            count[2] -= 1
            count[1] += 1
        j -= 1
    if(count[2] > m):
        while(j >= 0 and count[0] < m):
            if(a[j] == 2):
                a[j] = 0
                count[2] -= 1
                count[0] += 1
            j -= 1
if(count[1] > m):
    j = c = 0
    while(j < n and count[0] < m):
        if(a[j] == 1):
            a[j] = 0
            count[1] -= 1
            count[0] += 1
        j += 1
    i = j
    while(i < n and c <= m):
        if(a[i] == 1):
            c += 1
        i += 1
    j = i - 1
    if(count[1] > m):
        while(j < n and count[2] < m):
            if(a[j] == 1):
                a[j] = 2
                count[1] -= 1
                count[2] += 1
            j += 1
print("".join(map(str, a)))
