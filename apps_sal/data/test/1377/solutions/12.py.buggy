n = int(input())
l = [*list(map(int, input().split()))]
i = l.index(n)
left, right = i - 1, i + 1
cur = n - 1
while left >= 0 or right < n:
    if left >= 0 and l[left] == cur:
        left -= 1
        cur -= 1
    elif right < n and l[right] == cur:
        right += 1
        cur -= 1
    else:
        print("NO")
        return
print("YES")
