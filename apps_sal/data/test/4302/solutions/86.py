l = list(map(int, input().split()))
l.sort(reverse=True)
ans = l[0]
l[0] -= 1
l.sort(reverse=True)
print(ans + l[0])
