n, k = map(int, input().split())
d = list(map(int, input().split()))

count = [0] * k
for x in d:
    count[x%k] += 1

result = count[0]//2
for i in range(1, k):
    if i*2 >= k:
        break
    result += min(count[i], count[k-i])

if k%2==0:
    result += count[k//2]//2
print(result*2)
