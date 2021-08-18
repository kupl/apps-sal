N = int(input())
X_list = list(map(int, input().split()))

ans_list = []

for i in range(min(X_list), max(X_list) + 1):
    summarize = 0
    for x in X_list:
        summarize += (x - i)**2
    ans_list.append(summarize)

print(min(ans_list))
