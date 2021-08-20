import sys
input = sys.stdin.readline
(n, x) = map(int, input().split())
a_list = list(map(int, input().split()))
count = 0
if a_list[0] > x:
    count += a_list[0] - x
    a_list[0] -= a_list[0] - x
for i in range(len(a_list)):
    if i + 1 == len(a_list):
        break
    if a_list[i] + a_list[i + 1] > x:
        count += a_list[i] + a_list[i + 1] - x
        a_list[i + 1] -= a_list[i] + a_list[i + 1] - x
print(count)
