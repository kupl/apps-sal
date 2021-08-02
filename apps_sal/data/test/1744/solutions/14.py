n, m = list(map(int, input().split()))
t = list(map(int, input().split()))
freq = []
for i in range(101):
    freq.append(0)
for i in range(0, n):
    time = m - t[i]
    num = 0
    for j in range(1, 101):
        p = int(time / j)
        if(p >= freq[j]):
            time -= freq[j] * j
            num += freq[j]
        else:
            time -= p * j
            num += p
    print(i - num, end=" ")
    freq[t[i]] += 1
