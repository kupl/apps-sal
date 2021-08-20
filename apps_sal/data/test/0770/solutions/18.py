n = int(input())
is_unread = list(map(int, input().split()))
operations = 0
i = 0
while i < n and (not is_unread[i]):
    i += 1
if i < n:
    operations += 1
while i < n:
    delta = 1
    while i + delta < n and (not is_unread[i + delta]):
        delta += 1
    if i + delta < n:
        if delta == 1:
            operations += 1
        else:
            operations += 2
    i += delta
print(operations)
