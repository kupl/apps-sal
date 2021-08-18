n = int(input())
nums = list(map(int, input().split()))
print("YES" if (n * (n + 1)) / 2 == sum(nums) else "NO")
