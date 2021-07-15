N = int(input())
A = list(map(int, input().split()))
A_dict_list = []

for i in range(1, N+1):
    A_dict_list.append({
        'num': i,
        'people': A[i-1]
    })

A_dict_list = sorted(A_dict_list, key=lambda x:x['people'])

ans = []
for a in A_dict_list:
    ans.append(a['num'])

print((*ans))

