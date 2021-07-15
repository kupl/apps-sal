from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))

l = [0]
#累積和
for i in range(N):
    l.append(A[i]+l[i])
# print(l)

#Mの余りに変換
for i in range(N+1):
    l[i] %= M

c = Counter(l)
# print(c)
ans = 0
#同じ余り同士の区間は条件を満たす
for i in c.values():
    ans += i*(i-1)//2
print(ans)
