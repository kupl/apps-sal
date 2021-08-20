num = list(map(int, input().split()))
for _ in num:
    if num.count(_) == 2:
        print('Yes')
        break
    else:
        continue
else:
    print('No')
