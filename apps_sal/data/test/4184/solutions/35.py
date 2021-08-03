n = int(input())
li = list(map(int, input().split()))
su = []
for i in range(n):
    su.append(abs(sum(li[i:]) - sum(li[:i])))

print(min(su))
