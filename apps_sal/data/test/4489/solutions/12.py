N = int(input())
dic = {}
for i in range(N):
    word = input()
    if word in dic:
        dic[word] +=1
    else:
        dic[word] = 1
M = int(input())
for i in range(M):
    word = input()
    if word in dic:
        dic[word] -= 1
    else:
        dic[word] = -1

ans = 0#-float('inf')
for i in dic:
    ans = max(ans, dic[i])
print(ans)
