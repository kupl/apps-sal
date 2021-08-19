
# k=int(input())
# n,m=map(int,input().split())

# a=list(map(int,input().split()))

# b=list(map(int,input().split()))


def dfs(x):
    for s in range(1, cnt[x] + 1):
        if label[alp2[x][s]] == 0:
            label[alp2[x][s]] = label[x]
            dfs(alp2[x][s])


n = int(input())
a = input()
b = input()

l = n

alp = [0] * 27
alp2 = [0] * 27
cnt = [0] * 27
label = [-1] * 27

for i in range(27):
    alp[i] = [0] * 27
    alp2[i] = [0] * 27

for i in range(l):
    label[ord(a[i]) - ord('a') + 1] = 0
    label[ord(b[i]) - ord('a') + 1] = 0

cntlet = 0
for i in range(27):
    if label[i] == 0:
        cntlet += 1

for i in range(l):
    alp[ord(a[i]) - ord('a') + 1][ord(b[i]) - ord('a') + 1] = 1
    alp[ord(b[i]) - ord('a') + 1][ord(a[i]) - ord('a') + 1] = 1

for i in range(27):
    for j in range(i + 1, 27):
        if alp[i][j] == 1:
            cnt[i] += 1
            cnt[j] += 1
            alp2[i][cnt[i]] = j
            alp2[j][cnt[j]] = i

con = 0


for i in range(1, 27):
    if(label[i] == 0):
        con += 1
        label[i] = con
        dfs(i)

print(cntlet - con)

for i in range(1, con + 1):
    for j in range(1, 27):
        if label[j] == i:
            break

    for k in range(j + 1, 27):
        if label[k] == i:
            print(chr(j - 1 + ord('a')), chr(k - 1 + ord('a')))
