n = int(input())
nums = [int(x) for x in input().split()]
answers = set()

for i in range(n):
    cur_num = nums[i]
    furthest = max(n - i - 1, i)
    answers.add(cur_num // furthest)

if answers != set():
    print(min(answers))
else:
    print(0)
