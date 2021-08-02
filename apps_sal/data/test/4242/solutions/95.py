a, b, k = list(map(int, input().split()))
ans_list = []
for i in range(1, a + 1):
    if a % i == 0 and b % i == 0:
        ans_list.append(i)
print((ans_list[-k]))
