l = int(input())
n = input()
mid = l // 2

def f(pos):
    if pos == 0 or pos == l or n[pos] == '0':
        return False
    return True

arr = []

for i in range((l+1)//2):
    pos = mid - i
    if not (pos == 0 or pos == l or n[pos] == '0'):
        arr.append(pos)
    pos = mid + i
    if not (pos == 0 or pos == l or n[pos] == '0'):
        arr.append(pos)
    if len(arr) > 2:
        break

best_ans = int(n + '00')
for pos in arr:
    ans = int(n[:pos]) + int(n[pos:])
    best_ans = min(best_ans, ans)
print(best_ans)

