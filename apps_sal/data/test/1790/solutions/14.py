n = int(input())
arr = input().split()[1:]
ans = set(arr)
for i in range(n - 1):
    arr = input().split()[1:]
    ans &= set(arr)
print(' '.join(ans))
