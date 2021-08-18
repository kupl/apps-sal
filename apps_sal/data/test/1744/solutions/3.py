a = [int(i) for i in input().split()]
n = a[0]
M = a[1]
x = [int(i) for i in input().split()]
pref = [0 for i in x]
pref[0] = x[0]
freq = [0 for i in range(100)]
for i in range(1, n):
    pref[i] = pref[i - 1] + x[i]
for j in range(n):
    ans = pref[j]
    if(ans <= M):
        print(0, end=' ')
    else:
        k = 0
        while(ans > M):
            for i in range(99, -1, -1):
                if(freq[i] == 0):
                    continue
                y = (ans - M) // (i + 1)
                if(y == 0):
                    ans = ans - (i + 1)
                    k += 1
                elif(freq[i] <= y):
                    ans = ans - freq[i] * (i + 1)
                    k += freq[i]
                else:
                    if(ans - (y) * (i + 1) <= M):
                        ans = ans - (y) * (i + 1)
                        k += (y)
                    else:
                        ans = ans - (y + 1) * (i + 1)
                        k += (y + 1)
                if(ans <= M):
                    break
        print(k, end=' ')
    freq[x[j] - 1] += 1
