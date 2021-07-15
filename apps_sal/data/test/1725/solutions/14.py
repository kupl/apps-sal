array = []
n, m, d = input().split()
n, m, d = int(n), int(m), int(d)

for i in range(n):
    array += list(map(int, input().split()))
rem = array[0] % d
flag = False
for j in range(m*n):
    if array[j] % d != rem:
        flag = True
if flag:
    print('-1')
else:
    array.sort()
    median = len(array)//2
    ans = 0
    for i in range(n*m):
        val = array[i] - array[median]
        if val < 0:
            val = -val
        ans += val
    print(ans//d)
