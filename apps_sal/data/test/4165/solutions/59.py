n = int(input())
li = list(map(int, input().split()))
li.sort()
sum = 0
for a in li:
    sum += a
if sum - li[len(li) - 1] > li[len(li) - 1]:
    print("Yes")
else:
    print("No")
