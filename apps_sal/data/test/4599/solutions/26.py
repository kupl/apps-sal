N = int(input())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
Alice = []
Bob = []
i = 0
if N % 2 == 0:
    while i<=N-1:
        Alice.append(nums[i])
        Bob.append(nums[i+1])
        i += 2
else:
    while i<=N-2:
        Alice.append(nums[i])
        Bob.append(nums[i+1])
        i += 2
    Alice.append(nums[N-1])
sum_allice = sum(Alice)
sum_bob = sum(Bob)
answer = sum_allice - sum_bob
print(answer)
