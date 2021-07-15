S = input()
T = input()
count_list = []
count = 0
for i in range(len(S) - len(T) + 1):
    for j in range(len(T)):
        if T[j] == S[j + i]:
            count += 1
    count_list.append(count)
    count = 0
#print(count_list)
ans = len(T) - max(count_list)
print(ans)
