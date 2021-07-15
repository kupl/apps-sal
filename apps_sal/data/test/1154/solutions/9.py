#import sys
#sys.stdin = open("python/in", "r")

#n = int(input())
n, h, k = [int(i) for i in input().split(" ")]
arr = [int(i) for i in input().split(" ")]
arr.append(h)
ans = 0
ch = 0
i = 0
while True:
    while h - ch >= arr[i]:
        ch += arr[i]
        i += 1
    d, m = divmod(ch, k)
    ans += d
    if h - m >= arr[i]:
        ch = m
    else:
        ans += 1
        ch = 0
    if i == n:
        break
print(ans)

