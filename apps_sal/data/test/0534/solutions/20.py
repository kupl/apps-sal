a = input()
a = a.split(' ')
a = list(map(int, a))
n = a[0]
t = a[1]
queue = list(input())
for i in range(t):
    j = 0
    while (j < n - 1):
        if (queue[j] == 'B' and queue[j + 1] == 'G'):
            queue[j] = 'G'
            queue[j + 1] = 'B'
            j += 1
        j += 1
q = ''
for i in range(n):
    q = q + queue[i]
print(q)
