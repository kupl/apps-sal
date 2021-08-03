N = int(input())
L = list(map(int, input().split()))
sum = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            # print('i:'+str(i)+',j:'+str(j)+',k:'+str(k))
            if(L[i] + L[j] > L[k]) and (L[i] + L[k] > L[j]) and (L[j] + L[k] > L[i]) and (L[i] != L[j]) and (L[i] != L[k]) and (L[k] != L[j]):
                # print('a\n')
                sum += 1

print(sum)
