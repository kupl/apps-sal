N = int(input())
X_list = list(map(int, input().split()))

ans_list = []

for i in range(min(X_list), max(X_list)+1):
    summarize = 0
    # print(f'i：{i}')
    for x in X_list:
        summarize += (x-i)**2
        # print(f'i: {i}, x: {x}, summarize: {summarize}')
    ans_list.append(summarize)
    # print(f'ans_list: {ans_list}')

print(min(ans_list))
