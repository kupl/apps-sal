n, k = list(map(int, input().split()))
count = [0] * k
for c in input():
    count[ord(c) - ord("A")] += 1
print(k * min(count))
