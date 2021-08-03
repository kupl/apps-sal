import sys

n = int(input())

weight_list = list(map(int, input().split()))
diff = sys.maxsize

for i in range(n - 1):
    s_1 = sum(weight_list[:i + 1])
    s_2 = sum(weight_list[i + 1:])
    diff = min(diff, abs(s_1 - s_2))

print(diff)
