N, K = map(int, input().split())
count = 0
num_people = []
num_people_snacks = []
for i in range(1, N + 1):
    num_people.append(i)

while K > count:
    d = int(input())
    A = list(map(int, input().split()))
    for k in A:
        num_people_snacks.append(k)
    count += 1

ans = 0
for j in range(N):
    if num_people[j] not in num_people_snacks:
        ans += 1

print(ans)
