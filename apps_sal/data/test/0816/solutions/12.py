n, x = list(map(int, input().split()))
ip = list(map(int, input().split()))
count = 0
counts = [0 for i in range(100001)]
for i in ip:
    counts[i] += 1
for i in range(n):
    b = x ^ ip[i]
    counts[ip[i]] -= 1
    try:
        count += counts[b]
    except:
        b = 1
print(count)
