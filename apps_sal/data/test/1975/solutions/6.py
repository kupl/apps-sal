boys, girls = list(map(int, input().split()))
h = 1
i = 1
print(boys + girls - 1)
while h <= boys:
    while i <= girls:
        print(h, i)
        i += 1
    h += 1
    if h > boys:
        break
    print(h, i - 1)
