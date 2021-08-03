fd = open("input.txt", "r")
fd1 = open("output.txt", "w")
n = int(fd.readline())
arr = list(map(int, fd.readline().split()))
freq = [0 for i in range(5001)]
for i in range(n):
    freq[arr[i]] += 1
presum = [0 for i in range(5001)]
for i in range(1, 5001):
    presum[i] = presum[i - 1] + freq[i]
tot = n
mini = n
for i in range(1, 5001):
    maxa = 2 * i
    if maxa > 5001:
        break
    ans = n - (presum[maxa] - presum[i] + freq[i])
    mini = min(mini, ans)
fd1.write(str(mini))
