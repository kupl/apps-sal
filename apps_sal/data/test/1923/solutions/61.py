n = int(input())
llist = list(map(int, input().split()))
llist.sort()

ans = 0
for i in range(0, len(llist), 2):
    ans += llist[i]

print(ans)
