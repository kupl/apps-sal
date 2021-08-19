n = int(input())
tmp = 0
num_person = []
for _ in range(n):
    (l, r) = map(int, input().split())
    tmp = r - l + 1
    num_person.append(tmp)
ans = 0
for i in num_person:
    ans += i
print(ans)
