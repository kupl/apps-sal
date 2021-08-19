import sys
input_file = sys.stdin
n = int(input_file.readline())
lst = [0] + list((int(i) for i in input_file.readline().split())) + [1001]
maxi = 1
ans = 1
for i in range(1, len(lst)):
    if lst[i] == lst[i - 1] + 1:
        ans += 1
    else:
        maxi = max(maxi, ans)
        ans = 1
maxi = max(maxi, ans)
print(max(maxi - 2, 0))
