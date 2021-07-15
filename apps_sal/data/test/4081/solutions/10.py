n = int(input())
num = [*list(map(int, input().split()))]
ans = ""
current = -1
i = 0
j = n - 1
while True:
    if j < i:
        break
    if current < num[i] <= num[j] or num[j] <= current < num[i]:
        ans += "L"
        current = num[i]
        i += 1
        continue
    if current < num[j] <= num[i] or num[i] <= current < num[j]:
        ans += "R"
        current = num[j]
        j -= 1
        continue
    break
print(len(ans))
print(ans)

