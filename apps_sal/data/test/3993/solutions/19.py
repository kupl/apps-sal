n, m, k = map(int, input().split())
arr = map(int, input().split())
answer = 0
cur_page = -1
removed = 0
for i, el in enumerate(arr):
    if (el - removed - 1) // k != cur_page:
        answer += 1
        removed = i
        cur_page = (el - removed - 1) // k
print(answer)
