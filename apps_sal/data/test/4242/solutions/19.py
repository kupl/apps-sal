(a, b, k) = (int(i) for i in input().split())
list_ComDiv = []
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        list_ComDiv.append(i)
list_ans = sorted(list_ComDiv, reverse=True)
print(list_ans[k - 1])
