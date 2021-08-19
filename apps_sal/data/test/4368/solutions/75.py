(n, k) = list(map(int, input().split()))
answer = n // k
count = 1
while 0 < answer:
    answer = answer // k
    count += 1
print(count)
