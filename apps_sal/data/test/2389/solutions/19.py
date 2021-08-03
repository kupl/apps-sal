N, A, B, C = list(map(int, input().split()))
nums = [A, B, C]
steps = [input() for i in range(N)]
chars = ["A", "B", "C"]
operations = []
can_select = True
for i in range(N):
    s = steps[i]
    left_idx = chars.index(s[0])
    right_idx = chars.index(s[1])
    if (nums[left_idx] == 0 and nums[right_idx] == 0) or nums[left_idx] < 0 or nums[right_idx] < 0:
        can_select = False
        break
    elif nums[left_idx] == 1 and nums[right_idx] == 1 and i != N - 1:
        if chars[left_idx] in list(steps[i + 1]):
            nums[left_idx] += 1
            nums[right_idx] -= 1
            operations.append(chars[left_idx])
        else:
            nums[left_idx] -= 1
            nums[right_idx] += 1
            operations.append(chars[right_idx])
    else:
        if nums[left_idx] < nums[right_idx]:
            nums[left_idx] += 1
            nums[right_idx] -= 1
            operations.append(chars[left_idx])
        else:
            nums[left_idx] -= 1
            nums[right_idx] += 1
            operations.append(chars[right_idx])
if can_select:
    print("Yes")
    for i in operations:
        print(i)
else:
    print("No")
