n = int(input())
a = list(map(int, input().split()))
a = a[::-1]
hm = [0] * 10000
ans = []
for i in a:
    if(hm[i] == 0):
        ans.append(i)
        hm[i] = 1
print(len(ans))
for i in ans[::-1]:
    print(i, end=' ')
