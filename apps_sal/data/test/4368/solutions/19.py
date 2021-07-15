n, k = map(int, input().split())
lists = []

while True:
    if n < k:
        lists.append(n)
        break
    n, b = divmod(n, k)
    lists.append(b)

ans_list = reversed(lists)
print(len(''.join(map(str, ans_list))))
