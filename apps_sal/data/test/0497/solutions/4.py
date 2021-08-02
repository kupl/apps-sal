n = int(input())

colors = list(map(int, input().split()))

left = 0
right = n - 1
while colors[left] == colors[right]:
    left += 1

left_answer = right - left


left = 0
right = n - 1
while colors[left] == colors[right]:
    right -= 1

right_answer = right - left

print(max(left_answer, right_answer))
