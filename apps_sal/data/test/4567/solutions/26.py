n = int(input())
ll = []
for i in range(n):
    ll.append(int(input()))
ll.sort()
ans = sum(ll)
if ans % 10 == 0:
    for l in ll:
        if l % 10 != 0:
            print(ans - l)
            return
    print(0)
else:
    print(ans)
