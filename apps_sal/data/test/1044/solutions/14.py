def change(ans):
    if ans == 1:
        ans = 2
    else:
        ans = 1
    return ans


n = int(input())
array = list(map(int, input().split()))
if array[0] % 2 != 0:
    ans = 2
else:
    ans = 1
print(ans)
for i in range(1, n):
    if array[i] % 2 == 0:
        ans = change(ans)
    print(ans)
