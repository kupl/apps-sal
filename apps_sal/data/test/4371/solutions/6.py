

s = str(input())

abs_list = []

for i in range(1, len(s) - 1):
    x = int(s[i - 1: i + 2])
    abs_list.append(abs(x - 753))

answer = min(abs_list)
print(answer)
