N, K = map(int,input().split())
count = 0

while N >= 1:
    ans = N // K
    N = ans
    count += 1

print(count)
