N = int(input())
A = list(map(int, input().split()))
A = [i + 1 for i in A]

bucket = [0] * (10 ** 5 + 10)

for a in A:
    bucket[a - 1] += 1
    bucket[a] += 1
    bucket[a+1] += 1

print(max(bucket))
