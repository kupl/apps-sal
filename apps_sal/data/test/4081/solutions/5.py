import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

last = 0
left = 0
right = n - 1
ans = 0
output = []

while left <= right:
    if a[left] > last:
        if a[right] > last:
            if a[left] < a[right]:
                last = a[left]
                output.append('L')
                left += 1
            else:
                last = a[right]
                output.append('R')
                right -= 1
        else:
            last = a[left]
            output.append('L')
            left += 1
        ans += 1
    elif a[right] > last:
        last = a[right]
        output.append('R')
        right -= 1
        ans += 1
    else:
        break

print(ans)
print(''.join(output))
