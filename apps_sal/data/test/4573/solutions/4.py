n = int(input())
x = list(map(int, input().split()))
y = sorted(x)
#m = y[n//2-1:n//2+1]
m_index = n // 2 - 1
m = y[m_index]

for i in range(n):
    if x[i] <= m:
        print(y[m_index + 1])
    else:
        print(y[m_index])
