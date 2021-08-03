k = int(input())

n = 50
print(n)
nums = list(reversed(list(range(n))))

for i in range(n):
    nums[i] += k // n

for i in range(k % n):
    nums[i] += 1

t = list(map(str, nums))
print((' '.join(t)))
